# irrpi
Internet Remote Raspberry Pi  

Purpose is to have an internet connected raspberry pi run programs and be controlled through the internet without using port forwarding by having the pi check a website that you can control with instructions.  

The irrpi.service file should be copied by the user to /etc/systemd/system

## Quick Setup
git clone the project
  `git clone https://github.com/ssocolow/irrpi.git`

go into the directory of the project
  `cd irrpi`

edit the irrpi.service file to contain your working directory and file you want to be run on startup (change the path to whatever path you have for the irrpi.service file and the directory it is in) (read comments in irrpi.service)

run the setup script with sudo priveleges to allow it to enable and start the systemd unit file
  `sudo setup.sh`

now it should be running and you can check it with
  `systemctl status irrpi.service`

