# rclone Setup

1. Download and install
   curl https://rclone.org/install.sh | sudo bash

2. Config remote location
- config overview: rclone config
- Enter name: "nextcloud"
- Type of storage to configure: 38 (**Webdav**)
- url: https://empit-cloud-storage.com/remote.php/webdav/
- vendor: 1 (Nextcloud)
- user: EMPITCollab
- Password: asdh43sqa
  y (Yes type in my own password)
- bearer_token: <PRESS ENTER>
- Edit advanced config? n (no)
- Remote config overview: y (Yes this is OK)

# How to

rclone copy <src> <dest> --max-size 20M

das --max-size Argument excludiert beim download die Dateien, welche >= 20 mb sind. Ich vermute, dass es sich beim Upload ähnlich verhält.

bsp.:

rclone copy ~/Documents/Projects/lw nextcloud:/EMPIT_shared/lw_9Dec2021 --max-size 20M

Wenn special chars im Pfad oder Namen sind, dann →

rclone copy "~/Documents/Projects/lw special chars"  nextcloud:"/EMPIT_shared/lw_9Dec  2021"  --max-size 20M

	[[SOP]]