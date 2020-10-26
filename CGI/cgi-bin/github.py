#!/usr/bin/python3
print("Content-type: text/html")
print("")
import cgi
import subprocess
y=cgi.FieldStorage()
p=y.getvalue("profile")
r=y.getvalue("repo")
f=y.getvalue("file")
github_url="sudo curl https://raw.githubusercontent.com/{0}/{1}/master/{2} -o {2} -s".format(p,r,f)
out=subprocess.getstatusoutput(github_url)
if(out[0]==0):
	print("Yeah successfully downloaded!!!")
	print("Look for it in ur current directory")
else:
	print("Not successfull")

