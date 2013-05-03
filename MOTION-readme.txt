# instructions on how to install Motion for Streaming Live Feed from GrowPODs

#install motion
sudo apt-get install motion

# detect the device
lsusb

sudo nano /etc/motion/motion.conf
# edit the following entries
Daemon = OFF to ON
webcam_localhost = ON to OFF

sudo nano /etc/default/motion
#edit the following entries
start_motion_daemon=yes
sudo service motion start