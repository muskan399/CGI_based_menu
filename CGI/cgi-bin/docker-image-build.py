#!/usr/bin/python3
print("Content-type: text/html")
print("")
import cgi
import subprocess
form=cgi.FieldStorage()
cmd=form.getvalue('cmd')
img_name=form.getvalue('image')
new_img_name=form.getvalue('new_image')
print(cmd)
print(type(cmd))

