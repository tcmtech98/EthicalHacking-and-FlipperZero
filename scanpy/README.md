# scanpy

This program was developed for cybersecurity and pentesting purposes only!
<br><br>
This python file used to search for open ports on a specified host.
Most scanners do not include "local" resolving.
This was included to allow for future integration with Flipper Zero's BadUSB and RubberDucky.
<br><br>

# Syntax and Arguments
Using this basic framework, adjust the launching of the program accordingly:
<python/python3> scanpy.py <%host%|local> <common|port:%port%|port:x-y|port:x,y,z|file:%filename%>

#### <%host%|local>
  - %host% is replaced with the target's ip address
  - local refers to the computer's public ip address
#### common
  - program defines which ports to search through using common ports list
  - common ports: see list in section "Common Ports"
#### port
  - %port%: a single port to search for (ex: port:21)
  - x-y: a range of ports for searching, separated by a hyphen (ex: port:21-22)
  - x,y,z: a list of ports for searching, separated by a comma (ex: port:21,22,80)
#### file:%filename%
  - uses an external txt file for searching (ex: file:ports.txt)<br>

#### Example for Flipper Zero scripting (python3)
    python3 scanpy.py local common
#### Example for Flipper Zero scripting (python)
    python scanpy.py local common
You can take the examples a step futher by implementing the other arguments.
<br><br>

# External File Syntax
Any integers will be read by the system, everything else will be skipped.<br>
If the line starts with # (comment), the program will ignore the entire line.<br>
ports.txt is included as example, allowing you to comment out any ports that you won't be searching for.<br>
You can also add your own ports, including comments for future reference.<br>
#### Example external file:
    #FTP
    20
    21
    #SSH
    22
    #HTTP
    80
    8080
    #HTTPS
    443
    8443
    ...
#FTP will be ignored, while anything without "#" will be read.
<br><br>

# Common Ports
The program has built in "common ports" to search through when using the "common" argument.<br>
#### Common ports include:<br>
    20 - FTP
    21 - FTP
    22 - SSH
    23 - Telnet
    25 - SMTP
    53 - DNS
    80 - HTTP
    137 - NetBIOS over TCP
    139 - NetBIOS over TCP
    443 - HTTPS
    445 - SMB
    1433 - Database
    1434 - Database
    3306 - Database
    3389 - Remote Desktop
    8080 - HTTP
    8443 - HTTPS
<br><br>

# Flipper Zero Integration
Silent exfiltration will be available soon!

Please edit script files according to your specifications.<br>
Default configuration in the script file auto-closes CLI applications after 3 minutes after the program is launched by the script.
This ensures that whichever computer this is used on will not have any windows left open. <br>