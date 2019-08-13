#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")

data=cgi.FieldStorage()
cname=data.getvalue("cname")

subprocess.getoutput("sudo docker start {}".format(cname))

print("location: http://192.168.43.160/cgi-bin/menu/listdocker.py")
print()
