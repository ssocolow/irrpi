#!/usr/bin/env bash

#systemd doesn't like links apparently
#ln -s ./irrpi.service /etc/systemd/system

#get the path
OUT=$(pwd)
echo "${OUT}" 

systemctl enable "${OUT}/irrpi.service" 
systemctl start irrpi

