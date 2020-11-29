#!/usr/bin/env bash

while true; do
	echo 'service is working'
	git pull > pull.txt
	if grep -q Already /home/pi/programming/gpiostuff/irrpi/pull.txt; then
	       echo 'no update'
	else
 		echo 'update'
		python3 blink.py
	fi		
	sleep 5
done
