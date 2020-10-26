#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print("")
y=cgi.FieldStorage()
os=y.getvalue("os")
print("Output\n            ")
out=subprocess.getoutput("sudo docker inspect {0}".format(os))
print(out)

