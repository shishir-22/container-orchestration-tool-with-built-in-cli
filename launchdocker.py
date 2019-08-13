#!/usr/bin/python36

import cgi
import subprocess

print("content-type: text/html")
print()

data=cgi.FieldStorage()
dname=data.getvalue("dname")
docker=data.getvalue("list")

status=subprocess.getstatusoutput("sudo docker run -i -t -d --name "+dname+" "+docker)
if status[0]==0:
	print("Docker Launched successfully!!")
print("<br><form action='http://192.168.43.160/cgi-bin/menu/listdocker.py'>")
print("<input type='submit' value='Manage Containers'>")
print("</form>")
#print("<a href='http://192.168.43.161/cgi-bin/listdocker.py'>CLick here to manage docker instances</a>")

