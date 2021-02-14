#!/bin/bash

for i in $(seq 2 254); do
	#It redirects the output of ping to the /dev/null (the black hole)
	timeout 1 bash -c "ping -c 1 192.168.1.$i 2>/dev/null" && echo "Host 192.168.1.$i is ACTIVE" &
done; wait
