#!/usr/bin/python3
print("")
import cgi
import subprocess
form=cgi.FieldStorage()
os_name=form.getvalue('os')
cmd="sudo docker stop {0}".format(os_name)
cmd_out=subprocess.getstatusoutput(cmd)
status_code=cmd_out[0]
output=cmd_out[1]
if status_code==0000:
	print("YAYYYYYY container stopped")
else:
	print("Might be os name is not valid")

