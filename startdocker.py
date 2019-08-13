#!/usr/bin/python36

import subprocess

print("content-type: text/html")
print()

x=subprocess.getoutput("sudo docker images")
print("<form action='http://192.168.43.160/cgi-bin/menu/launchdocker.py'>")
print("Enter Docker Name:")
print("<input type='text' name='dname'><br>")
print("Select Docker Image:")
print("<select name='list'>")
for i in x.split("\n")[1:]:
	img=i.split()
	print("<option>"+img[0]+":"+img[1]+"</option>")
print("</select>")
print("<br><input type='submit'>")
print("</form>")
