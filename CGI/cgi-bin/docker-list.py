#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print("")
print("Output\n            ")
out=subprocess.getoutput("sudo docker ps")
print(out)


