#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print("")
y=cgi.FieldStorage()
os=y.getvalue("os")
image=y.getvalue("image")
port=y.getvalue("port")
print("Output is             ")
command="sudo docker run -dit -p {2}:{2} {1}".format(os,image,port)
out=subprocess.getoutput("sudo docker run -dit -p {2}:{2} {1}".format(os,image,port)
if out==0:
	print("Container launched successfully and port is alo exposed")0
else:
	print("Maybe u have written wrong image name or os name is already taken or port is busy")

