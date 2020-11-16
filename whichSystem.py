#!/usr/bin/python3

#re --> regular expressions
import re,sys, subprocess

#If user does not enter the ip address it will be notified.
if len(sys.argv) != 2:
	print("\n[!] Use: python3" + sys.argv[0] + "<ip-address>\n")
	sys.exit(1)

def get_ttl(ip_address):
	# It start a subprocess to launch a ping to the target, as we want to store the output in a variable
	# we'll need to set the stdout.
	# The shell is set to true because it will send the ping through the shell
	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell = True)
	
	# The output will be stored in out, if it is an error, it will be in err
	(out,err) = proc.communicate()

	#We split the output to have a simple filter
	out = out.split()

	#We decode the position 12 because it's ttl's position 
	out = out[12].decode('utf-8')
	
	#As out still has 'ttl=number' we'll delete  'ttl='
	ttl_value = re.findall(r"\d{1,3}", out) #1,3 because the number wont be bigger than 3  digits
	
	identify_ttl(int(ttl_value[0])) # ttl_value is a list

def identify_ttl(ttl_value):
	
	if ttl_value >= 0 and ttl_value <= 64:
		print("\n[!] OS --> Linux\n")
	elif ttl_value >=65 or ttl_value <= 128:
		print("\n[!] OS --> Windows\n")

if __name__ == '__main__':
	ip_address = sys.argv[1]
	
	print("\nIp address --> " + ip_address)
	get_ttl(ip_address)
