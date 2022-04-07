# Changes 25Jan22

spline_window.py

flatpak site packges  

```
/home/empit/.local/share/flatpak/app/app.empit.empit_lab_gps/current/active/files/lib/python3.9/site-packages  
```

```
from empit_db_project.db_helper_functions import copy_field_project
```

```
def get_reference_id_from_project(self, db, project):
        proj_id = project[0].database.project_id
        try:
            db_proj = DBFieldProject(proj_id, db)
        except Exception:
            remote_db = self.project[0].database.remote_db
            db_proj_remote = DBFieldProject(proj_id, remote_db)
            db_proj = copy_field_project(remote_db, db, db_proj_remote)
        try:
            new_proj = DBFieldProjectNew(db_proj.find_new_project_id(), db)
        except:
            new_proj = DBFieldProjectNew.from_old_DBFieldProject(db_proj)
        return new_proj
```

## Postgres Spline Setup

1. Install package on your OS with

```
podman pull docker.io/library/postgres:11
```

2. activate the default_env repo

3. then hack the postgres install steps of the 

```
/home/empit/Documents/empit_git_env/Wheels_24Jan22_Bruno/setup_local_postgresql_db.py
```

in vi ~/.zshrc

```
alias ipy="python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'"
```

in ipython (ipy)

## remove systemctl service

```bash
systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
rm /etc/systemd/system/[servicename] # and symlinks that might be related
rm /usr/lib/systemd/system/[servicename] 
rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed
```

### Fundamental Error

/home/empit/.local/share/flatpak/app/app.empit.empit_lab_gps/current/active/files/lib/python3.9/site-packages/empit_db_project/db_spline_segment.py

false (row 3 - 5)

```python
    @property
    def opt_result(self):
        # class Dummy:
        #     def __init__(self, f_xy, f_z, s):
        #         self.x = [f_xy, f_z, s]
```

correct  (input in row 18)

```python
class Dummy:
    def __init__(self, f_xy, f_z, s):
        self.x = [f_xy, f_z, s]
```

## current_mapper orange cube fix 15Feb22

`/home/empit/.local/share/flatpak/app/app.empit.empit_lab_gps/current/active/files/lib/python3.9/site-packages/empit_pipeline_spline/spline_tools/gps_filter.py`

substituted with

`/home/empit/Documents/empit_administration/Knowledgemanagement/Improvements/fp_3.9.30_spline_code_15Feb22/gps_filter.py`
