#!/bin/bash
#$1 takes the first argument passed when we execute the program, in this case should be the target ip-address
if [ $1 ]; then
	ipAddress=$1
	for port in $(seq 1 65535); do
		#It redirects the consult to the dev null (Linux black hole) to evade /dev/tcp stackoverflow
		#The last & means we are using threads to speed up the procces
		timeout 1 bash -c "echo '' > /dev/tcp/$ipAddress/$port" 2>/dev/null && echo "[*] The port $port is open" &
	done; wait
else
	echo -e "\n[*] Incorrect use, Try: ./portScan.sh <ip-address>\n"
	exit 1
fi
