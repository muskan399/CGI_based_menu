#!/usr/bin/python3
print("content-type: text/html")
print("")
import cgi
import subprocess
form=cgi.FieldStorage()
os_name=form.getvalue('os')
img_name=form.getvalue('image')
cmd="sudo docker run -dit --name {0} {1}".format(os_name,img_name)
cmd_out=subprocess.getstatusoutput(cmd)
status_code=cmd_out[0]
output=cmd_out[1]
if status_code==0000:
	print("YAYYYYYY container launched")
else:
	print("Might be os name or image name is not valid")
