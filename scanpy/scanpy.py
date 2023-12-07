import sys
import socket
import importlib.util
from datetime import datetime as dt

# Program: scanpy.py
# Description: used to search for open ports on a specified host
# Author: tcmtech98
# Website: tcmtech98.com
# GitHub: github.com/tcmtech98
# Version: 1.0
# Created: 12/5/23
# Last Modified: 12/7/23

# **NOTE**
# 	Be careful with lengthy searching, as it can take a VERY long time to gather results!

# Syntax: 
#	python scanpy.py {%host%|local} {common|port:%port%|port:x-y|port:x,y,z|file:%filename%}
#		Arguments:
#			-> {%host%|local}
#				- %host%: replaced with target's ip address
#				- local: refers to the computer's public ip address
#			-> common
#				- program defines which ports to search through using common ports list
#				- common ports: 20, 21, 22, 23, 25, 53, 80, 137, 139, 443, 445, 1433
#				  1434, 3306, 3389, 8080, 8443
#			-> port
#				- %port%: a single port to search for (ex: port:21)
#				- x-y: a range of ports for searching, separated by a hyphen (ex: port:21-22)
#				- x,y,z: a list of ports for searching, separated by a comma (ex: port:21,22,80)
#			-> file:%filename%
#				- uses an external txt file for searching (ex: file:ports.txt)

# .txt File Syntax:
#	int is recognized, anything else is not and will stop the program
#	using # at the start of a line ignores that line

# Common ports list:
#	20 - FTP
#	21 - FTP
#	22 - SSH
#	23 - Telnet
#	25 - SMTP
#	53 - DNS
#	80 - HTTP
#	137 - NetBIOS over TCP
#	139 - NetBIOS over TCP
#	443 - HTTPS
#	445 - SMB
#	1433 - Database
#	1434 - Database
#	3306 - Database
#	3389 - Remote Desktop
#	8080 - HTTP
#	8443 - HTTPS

commonPorts = [20, 21, 22, 23, 25, 53, 80, 137, 139, 443, 445, 1433, 1434, 3306, 3389, 8080, 8443]

# Prints help menu
def printHelp():
	print("\nSyntax: python3 scanpy.py {%host%|local} {common|port:%port%|port:x-y|port:x,y,z|file:%filename%}"
	+ "\n    Arguments:"
	+ "\n    -> {%host%|local}"
	+ "\n       - %host%: replaced with target's ip address"
	+ "\n       - local: refers to the computer's public ip address"
	+ "\n    -> common"
	+ "\n       - program defines which ports to search through using common ports list"
	+ "\n       - common ports: 20, 21, 22, 23, 25, 53, 80, 137, 139, 443, 445, 1433"
	+ "\n         1434, 3306, 3389, 8080, 8443"
	+ "\n    -> port"
	+ "\n       - %port%: a single port to search for (ex: port:21)"
	+ "\n       - x-y: a range of ports for searching, separated by a hyphen (ex: port:21-22)"
	+ "\n       - x,y,z: a list of ports for searching, separated by a comma (ex: port:21,22,80)"
	+ "\n    -> file:%filename%"
	+ "\n       - uses an external txt file for searching (ex: file:ports.txt)\n")

# Installs defined library
def install(package):
	import subprocess
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])
	print("\n\n\n")

# Searches for ports from given CLI arguments
def searchPort(target, x):
	i = 0
	if("-" in x):
		y = x.split("-")
		try:
			y[0] = int(y[0])
			y[1] = int(y[1])
		except ValueError:
			print("Error:", y[0], "and", y[1], "must be integers. Ex: ports:21-22")
			sys.exit()
		print("Scanning ports:", x)
		try:
			for port in range(y[0], y[1]):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,port))
				if result == 0:
					print(f"Port {port} is open")
					i += 1
				s.close()
			if(i == 0):
				print("No open ports were found on",ip)
		except KeyboardInterrupt:
			print("Program exiting...")
			sys.exit()
		except socket.error:
			print("Error: could not connect to server.")
	elif("," in x):
		y = x.split(",")
		try:
			for w in y:
				w = int(w)
		except:
			print("Error: all values in list must be an integer. Ex: ports:21,22,80,3066")
		try:
			for port in list(y):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,int(port)))
				if result == 0:
					print(f"Port {port} is open")
					i += 1
				s.close()
			if(i == 0):
				print("No open ports were found on",target)
		except KeyboardInterrupt:
			print("Program exiting...")
			sys.exit()
		except socket.error:
			print("Error: could not connect to server.")
	elif(x.lower() == "common"):
		print("Scanning ports:", commonPorts)
		try:
			for port in commonPorts:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,port))
				if result == 0:
					print(f"Port {port} is open")
					i += 1
				s.close()
			if(i == 0):
				print("No open ports were found on",ip)
		except KeyboardInterrupt:
			print("Program exiting...")
			sys.exit()
		except socket.error:
			print("Error: could not connect to server.")
	else:
		try:
			x = int(x)
			print("Scanning port:", x)
		except ValueError:
			print("Error:", x, "must be an integer. Ex: port:21")
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,x))
			if result == 0:
				print(f"Port {x} is open")
				i += 1
			s.close()
			if(i == 0):
				print("No open port was found on",ip)
		except socket.error:
			print("Error: could not connect to server.")	

# Searches for ports from file provided in CLI argument
def searchFile(target, x):
	j = 0;
	lines = []
	try:
		for line in open(x):
			li = line.strip()
			if not li.startswith("#"):
				try:
					a = int(li)
					if isinstance(a, int):
						lines.append(li)
				except:
					print("Error with data:", li + " is not an integer.")
	except:
		print("Error opening",x)
		sys.exit()
	if len(lines) == 0:
		print("Error: list is empty.")
		sys.exit()
	try:
		for y in lines:
			y = int(y)
	except:
		print("Error: all values in file must be an integer. Skips \"#\"")
	msg = ""
	if len(lines) > 1: msg = "Scanning ports:"
	else: msg = "Scanning port:"
	print(msg, str(lines).replace("'",""))
	try:
		for port in lines:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,int(port)))
			if result == 0:
				print(f"Port {port} is open")
				j += 1
			s.close()
		if(j == 0):
			print("No open ports were found on",target)
	except KeyboardInterrupt:
		print("Program exiting...")
		sys.exit()
	except socket.error:
		print("Error: could not connect to server.")

# Resolves ip from either local computer or given CLI argument
def assignTargetVal(x):
	target = ""
	if(x.lower() == "local"):
		if(importlib.util.find_spec('requests') is None):
			print("Library 'requests' is not installed, installing now!")
			install('requests')
		import requests
		target = requests.get('https://checkip.amazonaws.com').text.strip()
	else:
		try:
			target = socket.gethostbyname(x)
		except socket.gaierror:
			print("Error: invalid hostname.")
			sys.exit()
	msg = "Searching: " + target + " (" + x + ")"
	msg1 = len(msg) * "-"
	print(msg + "\n" + msg1)
	return target

# Message for invalid syntax or arguments
def invalid():
	print("Error: invalid syntax or arguments, type \"<python> scanpy.py help\" to receive a list of options.")
	sys.exit()

# Sends a banner
def banner():
	print("-" * 50)

# Main function
if (len(sys.argv) == 2) and (sys.argv[1].lower() == "help"):
	banner()
	printHelp()
	banner()
elif (len(sys.argv) == 3):
	banner()
	print("\nTime started:", str(dt.now()), "\n")
	target = assignTargetVal(sys.argv[1])
	if (":" in sys.argv[2]):
		a = sys.argv[2].split(":")
		if(a[0].lower() == "port"):
			searchPort(target, a[1])
		elif(a[0].lower() == "file"):
			searchFile(target, a[1])
		else:
			invalid()
	else:
		if(sys.argv[2].lower() == "common"):
			searchPort(target, "common")
		else:
			print("else")
			invalid()
	print("\nTime completed:", str(dt.now()), "\n")
	banner()
else:
	invalid()

# EDITS:
#	Make searchPorts() more efficient
#	Make searchFile() more efficient
#	Print services associated with port