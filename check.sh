#!/usr/bin/env bash

#get the path
OUT=$(pwd)


while true; do
	echo 'service is working'
	git pull > pull.txt
	if grep -q Already "${OUT}/pull.txt"; then
	       echo 'no update'
	else
 		echo 'update'
		python3 run.py
	fi		
	sleep 5
done
