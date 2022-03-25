#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:08:21 2021

@author: brunoschulz
"""
import os
import numpy as np
import copy
import scipy
import collections
import traceback
import pyproj
from pykalman import KalmanFilter
import pandas as pd
import pytz

import matplotlib.pyplot as plt

from empit_base import Data
from empit_lab.prepare_pitchroll import generate_pitchroll, geometry_pitchroll

try:
    from empit_lab.prepare_fullrot import generate_fullrot, geometry_fullrot
except ModuleNotFoundError:
    print("generate fullrotation not available")

from empit_coordinate_systems import EmpitCoordinateSystems


def fill_missing_positions(project, gps_measurements):
    # fill missing positions
    positions = project.get_base_data("gps_data").positions
    step = min(np.diff(positions))
    # test if step == 0
    assert step == 0, "step in positions is zero"

    grid = np.arange(positions[0], positions[-1], step)

    filled_gps_measurements = np.empty((len(grid), 3))
    filled_gps_quality = np.empty_like(grid)

    if len(positions) != len(grid):
        missing_positions = set(np.around(grid, 3)) - set(np.around(positions, 3))
        idx_missing = []
        for pos in missing_positions:
            idx_missing.append(np.where(np.around(grid, 3) == pos)[0])
        idx_missing = np.array(idx_missing).flatten()

        j = 0
        for i, pos in enumerate(grid):
            if i in idx_missing:
                filled_gps_measurements[i, :] = np.ma.masked
                filled_gps_quality[i] = 0.0
            else:
                filled_gps_measurements[i, :] = gps_measurements[j, :]
                filled_gps_quality[i] = project.gps.gps_data["quality"][j]
                j += 1

    return filled_gps_measurements, filled_gps_quality


class Geometry:
    def __init__(self, project, i_freq, i_shift=0):
        self.project = project
        self.i_freq = i_freq
        self.positions = project.positions
        self.i_shift = i_shift
        # self.yaw = self._get_yaw_rotation()

        if self.project.project_type == "EMPIT drone":
            df = self.project.db.get_df("cube")
            lat = df["lat_glob"].values[0]
            lon = df["lon_glob"].values[0]
            self.utm_zone = self._get_utm_zone_from_lon_lat(lon, lat)
        elif self.project.project_type == "EMPIT field":
            lon = self.project.get_base_data("gps_data")["longitude"][0]
            lat = self.project.get_base_data("gps_data")["latitude"][0]
            self.utm_zone = self._get_utm_zone_from_lon_lat(lon, lat)
        else:
            print("unknown vehicle type")
            raise NotImplementedError
            # self.utm_zone = self.project.gps.utm_zone

    # def _get_yaw_rotation(self):
    #     tilt_data = self.project.get_base_data('tilt_data')
    #     # modifying the tilt_data for the drone data
    #     if self.project.project_type == 'EMPIT drone':
    #         df = self.project.db.get_df('cube')
    #         tilt_data.positions = df['empit_meters'].values
    #         tilt_data['x'] = df['roll'].values
    #         tilt_data['y'] = df['pitch'].values
    #         print(f"## INFO: Created tilt data from cube\n{'-'*50}")
    #         print(f"## INFO Tilt, cube is DEG here --> converted to RAD!!\n{'-'*50}")

    #         self.project.sa_c.update_info({'tilt factors': [1.0, 1.0]})
    #         self.project.sa_c.update_info({'tilt shifts': [0.0, 0.0]})
    #         print(f"## INFO: set tilt factors and shifts to 1.0 and 0.0 respectively. \n Since the tilt_data is NOT a voltage but already an angle.\n{'-'*50}")

    #         # @todo this should be in a prepare task
    #         print(f"## INFO: Create geometry_pitchroll and b_fields_pitchroll\n{'-'*50}")
    #         generate_pitchroll(self.project)
    #         geometry_pitchroll(self.project)
    #         try:
    #             # generate_fullrot(self.project, i_shift=self.i_shift)
    #             # geometry_fullrot(self.project, i_shift=self.i_shift)

    #             generate_fullrot(self.project)
    #             geometry_fullrot(self.project)
    #         except:
    #             pass
    #         tilt_data.save()
    #         self.project.save()

    #         # read drone data
    #         self.rangefinder_alt = df['rangefinder_alt'].values
    #         self.radar_ground = df['radar_ground'].values
    #         self.radar_canopy = df['radar_canopy'].values

    #         # print('use global yaw approx. from df')
    #         # self.global_yaw = df['yaw'].values
    #         # self._set_utm_yaw_rotation(self.global_yaw)

    #     if self.project.from_db:
    #         print('set new coordinate systems')
    #         self.project.coord_sys = EmpitCoordinateSystems(
    #             self.project,
    #             self.project.sa_c,
    #             tilt_data,
    #             angles=True,
    #             local_yaw=0,
    #             i_freq=self.i_freq,
    #         )

    #     # legacy
    #     # voltage_ac = self.project.get_base_data('voltage_ac_vector')
    #     # self.project.coord_sys.read_tilt_data(tilt_data)
    #     # self.project.coord_sys.read_voltage_ac_vector(voltage_ac, i_freq=self.i_freq)

    #     yaw = self.project.coord_sys.rotation_yaw
    #     return yaw

    def _get_utm_zone_from_lon_lat(self, lon, lat):
        import utm

        _, _, zone, _ = utm.from_latlon(lat, lon)
        return zone

    # def _get_utm_yaw_rotation(self, pipeline):
    #     pipe_der = pipeline(pipeline.L_positions,der=1).T
    #     g_yaw_deg=(np.arctan2(pipe_der[:,1], pipe_der[:,0])*180./np.pi)
    #     # self.g_yaw = self.project.sa_c.get_yaw_rotation(g_yaw_deg, degrees=True)[0]
    #     self.g_yaw = self.project.sa_c.get_yaw_rotation(g_yaw_deg, degrees=True)[1]
    #     rot_x = scipy.spatial.transform.Rotation.from_euler('x', 180, degrees=True)
    #     # self.g_yaw_inv=[]
    #     for i in range(len(self.g_yaw)):
    #         # self.g_yaw[i] = (rot_x*self.g_yaw[i])
    #         # self.g_yaw_inv.append(self.g_yaw[i].inv())
    #         self.g_yaw[i] = self.g_yaw[i]*rot_x
    #     return self.g_yaw, g_yaw_deg

    def _set_utm_yaw_rotation(self, global_yaw, degrees=False):
        self.global_yaw = global_yaw
        self.g_yaw = self.project.sa_c.get_yaw_rotation(global_yaw, degrees=degrees)[1]
        rot_x = scipy.spatial.transform.Rotation.from_euler("x", 180, degrees=True)
        # self.g_yaw_inv=[]
        for i in range(len(self.g_yaw)):
            # self.g_yaw[i] = (rot_x*self.g_yaw[i])
            # self.g_yaw_inv.append(self.g_yaw[i].inv())
            self.g_yaw[i] = self.g_yaw[i] * rot_x
        return self.g_yaw, self.global_yaw

    #      (R_x*R_z_global_inv)**-1 = R_z_global*R_x_inv = R_z_global*R_x

    # R_z_global * R_x * R_z_local * R_pitchroll

    # r_x*r_z - r_x*r_z(-yaw)

    # def get_gps_antenna_rotated(self):
    #     if not hasattr(self, 'yaw'):
    #         self._get_yaw_rotation()
    #     if self.project.project_type == 'EMPIT drone':
    #         try:
    #             gps_height = abs(self.project.sa_c.info['gps_height'])
    #             gps_x = self.project.sa_c.info['cube_pos_x']
    #         except KeyError:
    #             gps_height = 0.35 #alte Drohne
    #             gps_x = 0.0
    #     elif self.project.project_type == 'EMPIT field':
    #         gps_height = self.project.gps_height
    #         gps_x = 0.0
    #     sa_c = self.project.sa_c
    #     gps_antenna = np.array([gps_x, 0, -gps_height])
    #     # @todo exchange to fullrot when full rotation is enabled
    #     gps_antenna_rotated = sa_c.apply_vector_rotation(gps_antenna, sa_c.rotation_pitchroll)
    #     gps_antenna_rotated = self.project.sa_c.apply_vector_rotation(gps_antenna_rotated, self.yaw)

    #     if self.project.project_type == 'EMPIT drone':
    #         try:
    #             lidar_offset = self.project.sa_c.info['lidar_height']
    #             radar_offset = self.project.sa_c.info['radar_height']
    #         except KeyError:
    #             lidar_offset = -0.15
    #             radar_offset = -0.15

    #         rangefinder_height = np.zeros((len(self.rangefinder_alt),3))
    #         rangefinder_height[:,2] = self.rangefinder_alt + lidar_offset
    #         rangefinder_height_pitchroll = sa_c.apply_vector_rotation(rangefinder_height, sa_c.rotation_pitchroll)

    #         radar_height = np.zeros((len(self.radar_ground),3))
    #         radar_height[:,2] = self.radar_ground + radar_offset
    #         radar_height_pitchroll = sa_c.apply_vector_rotation(radar_height, sa_c.rotation_pitchroll)

    #         canopy_height = np.zeros((len(self.radar_canopy),3))
    #         canopy_height[:,2] = self.radar_canopy + lidar_offset
    #         canopy_height_pitchroll = sa_c.apply_vector_rotation(canopy_height, sa_c.rotation_pitchroll)

    #         try:
    #             self.project.pipeline_spline._gps_data['rangefinder_height_pitchroll'] = rangefinder_height_pitchroll
    #             self.project.pipeline_spline._gps_data['ground_height_pitchroll'] = radar_height_pitchroll
    #             self.project.pipeline_spline._gps_data['canopy_height_pitchroll'] = canopy_height_pitchroll
    #         except AttributeError:
    #             print('PipelineSpline Project has no self._gps_data  -->  set a "key" and call self.gps_data')

    #     return gps_antenna_rotated

    def rotate_drone_heights(self):
        # TODO: needs to go into the sa_c object
        try:
            lidar_offset = (0.17, -0.05, self.project.sa_c.info["lidar_height"])
            radar_offset = (0.16, 0.07, self.project.sa_c.info["radar_height"])
        except KeyError:
            lidar_offset = (0.17, -0.05, -0.15)
            radar_offset = (0.16, 0.07, -0.15)

        try:
            pitch = self.project.get_base_data("geometry_pipe_fit")["pitch"][
                self.i_freq
            ]
        except:
            pitch = np.zeros(self.project.n_positions)

        # read drone data
        df = self.project.database.local_db.get_df("cube")
        self.rangefinder_alt = df["rangefinder_alt"].values
        self.radar_ground = df["radar_ground"].values
        self.radar_canopy = df["radar_canopy"].values

        rangefinder_height = np.zeros((len(self.rangefinder_alt), 3))
        rangefinder_height[:, 2] = (
            self.rangefinder_alt + lidar_offset[2] - np.tan(pitch) * lidar_offset[0]
        )
        rangefinder_height_pitchroll = self.project.coord_sys.local_to_local_pitchroll(
            rangefinder_height
        )

        radar_height = np.zeros((len(self.radar_ground), 3))
        radar_height[:, 2] = (
            self.radar_ground + radar_offset[2] - np.tan(pitch) * radar_offset[0]
        )
        radar_height_pitchroll = self.project.coord_sys.local_to_local_pitchroll(
            radar_height
        )

        canopy_height = np.zeros((len(self.radar_canopy), 3))
        canopy_height[:, 2] = (
            self.radar_canopy + lidar_offset[2] - np.tan(pitch) * lidar_offset[0]
        )
        canopy_height_pitchroll = self.project.coord_sys.local_to_local_pitchroll(
            canopy_height
        )

        try:
            self.project.pipeline_spline._gps_data[
                "rangefinder_height_pitchroll"
            ] = rangefinder_height_pitchroll
            self.project.pipeline_spline._gps_data[
                "ground_height_pitchroll"
            ] = radar_height_pitchroll
            self.project.pipeline_spline._gps_data[
                "canopy_height_pitchroll"
            ] = canopy_height_pitchroll
        except AttributeError:
            print(
                'PipelineSpline Project has no self._gps_data  -->  set a "key" and call self.gps_data'
            )

    # def get_utm_pipeline_data(self, gps_antenna, pipeline):
    #     i_freq = self.i_freq

    #     lateral_offset = self.project.get_base_data('geometry_pitchroll')['lateral_offset'][i_freq,:]
    #     depth = self.project.get_base_data('geometry_pitchroll')['depth'][i_freq,:]

    #     gps_data_local = self.get_gps_antenna_rotated()
    #     gps_track_local = copy.deepcopy(gps_data_local)

    #     # if self.project.project_type == 'EMPIT drone':
    #         # print('drone: ==> take - lateral_offset')
    #         # lateral_offset *= -1
    #     #     lateral_offset = self.project.get_base_data('geometry_full')['lateral_offset'][i_freq,:]
    #     #     depth = self.project.get_base_data('geometry_full')['depth'][i_freq,:]

    #     gps_data_local[:,1] -= lateral_offset
    #     gps_data_local[:,2] -= depth

    #     # Rotate the corrected pitch, roll and yaw local system into the global utm system
    #     if not hasattr(self, 'g_yaw'):
    #         _, utm_yaw = self._get_utm_yaw_rotation(pipeline)
    #     else:
    #         utm_yaw = self.global_yaw
    #     gps_data_local = self.project.sa_c.apply_vector_rotation(gps_data_local, self.g_yaw)
    #     gps_track_local = self.project.sa_c.apply_vector_rotation(gps_track_local, self.g_yaw)
    #     # gps_data_local = self.project.sa_c.apply_vector_rotation(gps_data_local, self.g_yaw2)
    #     # gps_track_local = self.project.sa_c.apply_vector_rotation(gps_track_local, self.g_yaw2)

    #     gps_data = gps_antenna - gps_data_local
    #     gps_track = gps_antenna - gps_track_local

    #     return gps_data, gps_track, utm_yaw

    # using EmpitCoordinateSystem
    def get_utm_pipeline_data_new(
        self, gps_antenna, pipeline, datatype="geometry_pitchroll", gps_key=None
    ):
        i_freq = self.i_freq

        get_pipe_rotation_from = "geometry_pipe_fit"
        if self.project.from_db:
            get_pipe_rotation_from = "rotation_fitter"

        try:
            gps_positions = self.project.antenna_position(gps_key)
        except NotImplementedError:
            gps_positions = self.project.antenna_position()

        print("here:", get_pipe_rotation_from)
        print("set utm pipeline_data, i_freq:{}", i_freq)
        coord_sys = EmpitCoordinateSystems.new_from_project(
            self.project,
            i_freq=self.i_freq,
            get_pipe_rotation_from=get_pipe_rotation_from,
            antenna_position=gps_positions,
        )

        if not hasattr(self, "g_yaw"):
            utm_yaw = coord_sys.get_global_yaw_approx_from_pipeline(pipeline)
        else:
            utm_yaw = self.global_yaw

        coord_sys.set_utm_rotation(utm_yaw, degrees=False)
        coord_sys.get_local_origin_in_utm(gps_antenna)

        track_data = coord_sys.local_to_global(np.array([0.0, 0.0, 0.0]))
        pipeline_data = coord_sys.get_pipeline_from_antenna(
            gps_antenna, datatype=datatype
        )

        return pipeline_data, track_data, utm_yaw

    # # @todo use track data instead the pipeline
    # def get_utm_sensor_positions(self, pipeline):
    #     i_freq = self.i_freq
    #     pos = self.project.sa_c.sensor_coords_pitchroll
    #     #test
    #     # self.project.sa_c.sensor_coords_vector[0] = np.array([0.0, 0.0, -self.project.gps_height])
    #     # pos = np.array([self.project.sa_c.apply_vector_rotation(self.project.sa_c.sensor_coords_vector, rot) for rot in self.project.sa_c.rotation_pitchroll])
    #     #test ende

    #     pos = self.project.sa_c.apply_vector_rotation(pos, self.yaw)

    #     lateral_offset = self.project.get_base_data('geometry_pitchroll')['lateral_offset'][i_freq,:]
    #     pos[:,:,1] -= lateral_offset.repeat(self.project.sa_c.n_vectors).reshape(-1,self.project.sa_c.n_vectors)
    #     depth = pipeline.data['ground']
    #     pos[:,:,2] -= depth.repeat(self.project.sa_c.n_vectors).reshape(-1,self.project.sa_c.n_vectors)
    #     # Rotate the corrected pitch, roll and yaw local system into the global utm system
    #     if not hasattr(self, 'g_yaw'):
    #         self._get_utm_yaw_rotation(pipeline)
    #     pos = self.project.sa_c.apply_vector_rotation(pos, self.g_yaw)

    #     pipe_sp = pipeline(pipeline.L_positions,der=0).T

    #     pos2 = np.empty_like(pos)
    #     pos2[:,:,2] = pos[:,:,2]
    #     # depth = pipeline.data['ground']
    #     for i in range(pos.shape[0]):
    #         pos[i,:,0] += pipe_sp[i,0]
    #         pos[i,:,1] += pipe_sp[i,1]

    #         # pos2[i,:,0] = pipe_sp[i,0] - pos[i,:,0]
    #         # pos2[i,:,1] = pipe_sp[i,1] - pos[i,:,1]

    #         # pos[i,:,2] += pipe_sp[i,2] + depth[i]
    #         # pos[i,:,2] += depth[i]

    #     return pos

    def get_geoid_separation_from_gps_log(self):
        import pynmea2
        import datetime

        cube = self.project.database.local_db.get_df("cube")
        year = cube["dt_main"][0].year
        month = cube["dt_main"][0].month
        day = cube["dt_main"][0].day

        gps_msg_timestamp = []
        with open(os.path.join(self.project.datadirname, "gps_log")) as f:
            for line in f.readlines():
                try:
                    msg = pynmea2.parse(line)

                    hour = msg.timestamp.hour
                    minute = msg.timestamp.minute
                    second = msg.timestamp.second
                    microsecond = msg.timestamp.microsecond
                    timestamp = pd.Timestamp(
                        datetime.datetime(
                            year, month, day, hour, minute, second, microsecond
                        )
                    )
                    geoid_sep = float(msg.geo_sep)
                    gps_msg_timestamp.append([timestamp, geoid_sep])
                except pynmea2.ParseError as e:
                    print("Parse error: {}".format(e))
                    continue

        gpslog_df = pd.DataFrame(gps_msg_timestamp)
        return np.array(
            [gpslog_df[1][abs(gpslog_df[0] - ts).argmin()] for ts in cube["dt_main"]]
        )

    def get_gps_data_from_base(self):
        project = self.project
        if project.project_type == "EMPIT drone":
            try:
                try:
                    conversion_factor = project.sa_c.info["conversion_factor"]
                except:
                    conversion_factor = 1000
                df = project.db.get_df("cube")
                gps_data = Data(positions=df["empit_meters"].values)
                # gps_data["latitude"] = df["lat_glob"].values
                # gps_data["longitude"] = df["lon_glob"].values
                # gps_data["alt_raw"] = df["alt_raw"].values / conversion_factor
                lat1 = df["lat_raw"].values
                lon1 = df["lon_raw"].values
                alt1 = df["alt_raw"].values / conversion_factor
                lat2 = df["lat2_raw"].values
                lon2 = df["lon2_raw"].values
                alt2 = df["alt2_raw"].values / conversion_factor
                gps_data["latitude"] = np.mean([lat1, lat2], axis=0)
                gps_data["longitude"] = np.mean([lon1, lon2], axis=0)
                gps_data["alt_raw"] = np.mean([alt1, alt2], axis=0)
                gps_data["satelites"] = df["sat_vis"].values
                gps_data["quality"] = df["fix_type"].values
                gps_data["rangefinder_alt"] = df["rangefinder_alt"].values
                gps_data["radar_ground"] = df["radar_ground"].values
                gps_data["radar_canopy"] = df["radar_canopy"].values
                print(f"## INFO: Created gps data from cube\n{'-'*50}")

                try:
                    gps_data["geoid_separation"] = df["geoid_separation"].values
                except:
                    gps_data[
                        "geoid_separation"
                    ] = self.get_geoid_separation_from_gps_log()

                gps_data["alt_ellips"] = (
                    gps_data["alt_raw"] + gps_data["geoid_separation"]
                )

            except:
                print(f'## Reading gps_data, tilt_data from database failed\n{"-"*50}')
                traceback.print_exc()
            # gps_data = gps.project.get_base_data('gps_data')
            # tilt_data = gps.project.get_base_data('tilt_data')
        else:
            try:
                gps_data = project.get_base_data("gps_data")
            except (KeyError, FileNotFoundError):
                project.prepare()
                project.save()
                gps_data = project.get_base_data("gps_data")

        positions = gps_data.positions
        gps_quality = gps_data["quality"]

        p_utm_to_wgs = pyproj.Proj(proj="utm", ellps="WGS84", zone=self.utm_zone)
        x, y = p_utm_to_wgs(gps_data["longitude"], gps_data["latitude"])
        gps_measurements = np.array([x, y, gps_data["alt_ellips"]]).T

        return positions, gps_measurements, gps_quality

    def get_gps_data_cube(self, gps_key, geo_sep=0):
        """
        Overwrites the gps_data with the mapped gps information from the CUBE
        """

        cube = self.project.database.local_db.get_df("cube")

        gps_data = self.project.get_base_data("gps_data")

        gps_data_raw = []
        gps_quality_raw = []

        sa_list = self.project.sa_a_list
        for sa in sa_list:
            start = sa.starttime
            end = sa.endtime

            cube_time = cube["dt_main"]

            measurement_point = cube.loc[
                (cube["dt_main"].dt.tz_localize(pytz.utc) >= start)
                & (cube["dt_main"].dt.tz_localize(pytz.utc) <= end)
            ]

            if gps_key == "cube":
                lat_median = np.median(measurement_point["lat_glob"].values)
                lon_median = np.median(measurement_point["lon_glob"].values)
                alt_median = np.median(measurement_point["alt_glob"].values)
            elif gps_key == "left":
                lat_median = np.median(measurement_point["lat_raw"].values)
                lon_median = np.median(measurement_point["lon_raw"].values)
                alt_median = np.median(measurement_point["alt_raw"].values)
            elif gps_key == "right":
                lat_median = np.median(measurement_point["lat2_raw"].values)
                lon_median = np.median(measurement_point["lon2_raw"].values)
                alt_median = np.median(measurement_point["alt2_raw"].values)
            else:
                raise NotImplementedError

            # quality = np.median(measurement_point["fix_type"].values)
            quality = 4
            try:
                geo_sep = np.median(measurement_point["geoid_separation"].values)
            except:
                pass

            gps_data_raw.append([lat_median, lon_median, alt_median + geo_sep])
            gps_quality_raw.append(quality)

        gps_data_raw = np.array(gps_data_raw)
        gps_quality_raw = np.array(gps_quality_raw)

        gps_data["latitude"] = gps_data_raw[:, 0]
        gps_data["longitude"] = gps_data_raw[:, 1]
        gps_data["alt_ellips"] = gps_data_raw[:, 2]
        gps_data["quality"] = gps_quality_raw

        gps_data.save()

        positions = gps_data.positions
        gps_quality = gps_data["quality"]

        p_utm_to_wgs = pyproj.Proj(proj="utm", ellps="WGS84", zone=self.utm_zone)
        x, y = p_utm_to_wgs(gps_data["longitude"], gps_data["latitude"])
        gps_measurements = np.array([x, y, gps_data["alt_ellips"]]).T

        return positions, gps_measurements, gps_quality

    def apply_gps_filter(
        self,
        project,
        gps_measurements,
        gps_quality,
        gps_accuracy=[0.1, 0.1, 0.2],
        factor=1e7,
        mixing=[0, 1],
        indicator=4,
    ):
        gps_filter = GPSFilter(
            gps_measurements, gps_quality, gps_accuracy, mixing, factor, indicator
        )

        # filter in both directions
        state_means_forward, state_errors_forward = gps_filter.filter()
        state_means_backward, state_errors_backward = gps_filter.filter(reverse=True)

        # average between the both directions
        state_means = []
        state_errors = []
        for i in range(6):
            state_means.append(
                np.average(
                    [state_means_forward[:, i], state_means_backward[:, i]],
                    weights=[
                        1 / state_errors_forward[:, i] ** 2,
                        1 / state_errors_backward[:, i] ** 2,
                    ],
                    axis=0,
                )
            )
            state_errors.append(
                np.average(
                    [state_errors_forward[:, i], state_errors_backward[:, i]], axis=0
                )
            )

        state_means = np.array(state_means).T
        state_errors = np.array(state_errors).T

        # only return position coordinates the velocities are not needed
        return state_means[:, :3], state_errors[:, :3]

    # def perform_pitchroll_rotation(self, project, gps_track):
    #     gps_height = project.gps_height
    #     sa_c = project.sa_c

    #     if project.project_type == 'EMPIT drone':
    #         df = project.db.get_df('cube')
    #         rangefinder_alt = df['rangefinder_alt'].values
    #         radar_ground = df['radar_ground'].values
    #         radar_canopy = df['radar_canopy'].values

    #         tilt_data = project.get_base_data('tilt_data')
    #         tilt_data.positions = df['empit_meters'].values

    #         # tilt_data = Data(positions=df['empit_meters'].values)
    #         tilt_data['x'] = df['roll'].values*np.pi/180
    #         tilt_data['y'] = df['pitch'].values*np.pi/180
    #         print(f"## INFO: Created tilt data from cube\n{'-'*50}")
    #         print(f"## INFO Tilt, cube is DEG here --> converted to RAD!!\n{'-'*50}")

    #         sa_c.update_info({'tilt factors': [1.0, 1.0]})
    #         sa_c.update_info({'tilt shifts': [0.0, 0.0]})
    #         print(f"## INFO: set tilt factors and shifts to 1.0 and 0.0 respectively. \n Since the tilt_data is NOT a voltage but already an angle.\n{'-'*50}")

    #         # @todo this should be in a prepare task
    #         print(f"## INFO: Create geometry_pitchroll and b_fields_pitchroll\n{'-'*50}")
    #         generate_pitchroll(project)
    #         geometry_pitchroll(project)
    #         project.save()

    #     elif project.project_type == 'EMPIT field':
    #         tilt_data = project.get_base_data('tilt_data')

    #     sa_c.read_tilt_data(tilt_data)
    #     rotation_pitchroll = sa_c.rotation_pitchroll

    #     if project.project_type == 'EMPIT drone':
    #         print('drone project')
    #         # @todo use correct gps height
    #         # gps_height = project.gps_height
    #         gps_height = 0.35
    #         lidar_offset = -0.15
    #         radar_offset = -0.15

    #         rangefinder_height = np.zeros_like(gps_track)
    #         rangefinder_height[:,2] = rangefinder_alt + lidar_offset

    #         radar_height = np.zeros_like(gps_track)
    #         radar_height[:,2] = radar_ground + radar_offset

    #         radar_canopy_height = np.zeros_like(gps_track)
    #         radar_canopy_height[:,2] = radar_canopy + radar_offset

    #         gps_antenna = np.array([0, 0, -gps_height])
    #     elif project.project_type == 'EMPIT field':
    #         gps_antenna = np.array([0, 0, -gps_height])

    #     gps_antenna_pitchroll = sa_c.apply_vector_rotation(gps_antenna, rotation_pitchroll)
    #     gps_track_corrected = gps_track + gps_antenna_pitchroll

    #     if project.project_type == 'EMPIT drone':
    #         rangefinder_height_pitchroll = sa_c.apply_vector_rotation(rangefinder_height, rotation_pitchroll)
    #         project.pipeline_spline._gps_data['rangefinder_height_pitchroll'] = rangefinder_height_pitchroll

    #         radar_height_pitchroll = sa_c.apply_vector_rotation(radar_height, rotation_pitchroll)
    #         project.pipeline_spline._gps_data['radar_height_pitchroll'] = radar_height_pitchroll

    #         radar_canopy_height_pitchroll = sa_c.apply_vector_rotation(radar_canopy_height, rotation_pitchroll)
    #         project.pipeline_spline._gps_data['radar_canopy_height_pitchroll'] = radar_canopy_height_pitchroll

    #     return gps_track_corrected

    # def calc_pipeline_data_points(self, project, pipeline, gps_track, i_freq):
    #     '''
    #     prefactor in lateral_offset
    #     '''
    #     geo_pitchroll = project.get_base_data('geometry_pitchroll')
    #     lat_factor = 1.0
    #     depth = geo_pitchroll['depth'][i_freq]
    #     lateral_offset = geo_pitchroll['lateral_offset'][i_freq]

    #     L = pipeline.L_positions
    #     data = []
    #     for i, l in enumerate(L):
    #         _, ey, _ = pipeline.local_system(l)

    #         r = np.array([gps_track[i,0],
    #                       gps_track[i,1],
    #                       gps_track[i,2] - depth[i]]) + lat_factor*lateral_offset[i]*ey.flatten()
    #         data.append(r)
    #     return np.array(data)


class GPSFilter:
    """
    Filter the GPS data based on a Kalman filter
    For further information the the docs from pykalman
    """

    def __init__(
        self,
        gps_measurements,
        gps_quality,
        gps_uncertainty,
        mixing=[0, 1],
        factor=1e6,
        indicator=4,
    ):
        """
        Parameters
        ----------
        gps_measurements : array_like
                           Array containing the GPS data in a shape (n,3)
                           where n is the number of data points. The data should
                           be in utm coordinates to work properly
        gps_quality : array_like
                           GPS indicator for each measurement point used for
                           dynamically changing the observation covariance matrix
                           in each step of the Kalman filter

        indicator : int
                           GPS indicator describing the RTK-Fix mode of the GPS
                           indicator == 4 <==> RTK-Fix
        gps_uncertainty : array (3,)
                           Array containing the uncertainties of the GPS in the
                           case of RTK-Fix for x, y and z
        mixing : array (2,)
                           Mixing of the dynamical state covariance and the gps_quality
                           [0, 1] ==> 0*gps_quality + 1*state_covariance
        factor : float or array
                    float: A number which is multiplied by the gps_quality if the
                           GPS indicator is not RTK-Fix
                    array: A number for each measurment step which is multiplied by
                           the gps_quality
        """
        self.gps_measurements = gps_measurements
        self.gps_uncertainty = gps_uncertainty
        if gps_quality is None:
            self.gps_quality = np.ones(len(gps_measurements))
        else:
            self.gps_quality = gps_quality
        self.indicator = indicator
        self.mixing = mixing

        self.factor = factor

        # transition matrix
        self.F = np.array(
            [
                [1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 1],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )

        # measurement matrix
        self.H = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]])

        self.R1 = np.diag(self.gps_uncertainty) ** 2

        if isinstance(factor, (collections.Sequence, np.ndarray)):
            self.use_sequence = True
            self.R2 = [self.R1 * value ** 2 for value in factor]
        else:
            self.use_sequence = False
            self.R2 = self.R1 * factor ** 2

        self.kf = KalmanFilter(transition_matrices=self.F, observation_matrices=self.H)

    def filter(self, reverse=False):
        """
        Parameter
        ---------
        reverse : bool
                  Whether the data should be processed in reverse order

        Returns
        -------
        filtered_gps_measurements : array_like (gps_measurements(input))
        estimated_gps_errors : array_like (gps_measurements(input))
        """

        gps_filtered = []
        gps_errors = []

        R = self.R1

        if reverse:
            gps_quality = self.gps_quality[::-1]
            gps_measurements = self.gps_measurements[::-1]
            if self.use_sequence:
                R2 = self.R2[::-1]
            else:
                R2 = self.R2
        else:
            gps_quality = self.gps_quality
            gps_measurements = self.gps_measurements
            R2 = self.R2

        # initial states
        state_mean = np.hstack([gps_measurements[0, :], 3 * [0.0]])
        state_cov = np.diag(np.array([self.gps_uncertainty, 3 * [1e-6]]).flatten())

        for i, (quality, measurement) in enumerate(zip(gps_quality, gps_measurements)):
            if quality != self.indicator and not self.use_sequence:
                R = R2
            elif self.use_sequence:
                R = R2[i]

            state_mean, state_cov = self.kf.filter_update(
                state_mean, state_cov, observation=measurement, observation_covariance=R
            )

            R = np.average([self.R1, state_cov[:3, :3]], axis=0, weights=self.mixing)

            gps_filtered.append(state_mean)

            error_estimate = [np.sqrt(state_cov[i, i]) for i in range(6)]
            gps_errors.append(error_estimate)

        gps_means, gps_error_estimates = np.array(gps_filtered), np.array(gps_errors)
        if reverse:
            gps_means = gps_means[::-1]
            gps_error_estimates = gps_error_estimates[::-1]
        return gps_means, gps_error_estimates

    def filter_fit(self, reverse=False):
        """
        Parameter
        ---------
        reverse : bool
                  Whether the data should be processed in reverse order

        Returns
        -------
        filtered_gps_measurements : array_like (gps_measurements(input))
        estimated_gps_errors : array_like (gps_measurements(input))
        """

        gps_filtered = []
        gps_errors = []

        R = self.R1

        if reverse:
            gps_quality = self.gps_quality[::-1]
            gps_measurements = self.gps_measurements[::-1]
            if self.use_sequence:
                R2 = self.R2[::-1]
            else:
                R2 = self.R2
        else:
            gps_quality = self.gps_quality
            gps_measurements = self.gps_measurements
            R2 = self.R2

        # initial states
        state_mean = np.hstack([gps_measurements[0, :], 3 * [0.0]])
        state_cov = np.diag(np.array([self.gps_uncertainty, 3 * [1e-6]]).flatten())

        R_old = self.R1

        for i, (quality, measurement) in enumerate(zip(gps_quality, gps_measurements)):
            if quality != self.indicator and not self.use_sequence:
                R = R2
            elif self.use_sequence:
                R = np.average([R2[i], R_old], weights=[0.33, 0.66], axis=0)

            state_mean, state_cov = self.kf.filter_update(
                state_mean, state_cov, observation=measurement, observation_covariance=R
            )

            R_old = np.average(
                [self.R1, state_cov[:3, :3]], axis=0, weights=self.mixing
            )

            gps_filtered.append(state_mean)

            error_estimate = [np.sqrt(state_cov[i, i]) for i in range(6)]
            gps_errors.append(error_estimate)

        gps_means, gps_error_estimates = np.array(gps_filtered), np.array(gps_errors)
        if reverse:
            gps_means = gps_means[::-1]
            gps_error_estimates = gps_error_estimates[::-1]
        return gps_means, gps_error_estimates
