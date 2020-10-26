#!/usr/bin/python3
print("content-type: text/html")
print("")
import cgi
import subprocess
import json
form=cgi.FieldStorage()
instance_type=form.getvalue('instance_type')
image=form.getvalue('image')
if (image=="redhat"):
	ami="ami-052c08d70def0ac62"
elif(image=="ubuntu"):
	ami="ami-0cda377a1b884a1bc"
elif(image=="amazon linux2"):
	ami="ami-0e306788ff2473ccb"
else:
	ami="ami-03cfb5e1fb4fac428"
instance_type="t2.micro"

cmd="AWS_ACCESS_KEY_ID=AKIA26T7HQNFTLXTSX7T AWS_SECRET_ACCESS_KEY=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 aws ec2 run-instances --image-id {0} --count 1 --instance-type {1} --security-group-ids sg-00b59370d35349eaa --region ap-south-1".format(ami,instance_type)
cmd_out=subprocess.getstatusoutput(cmd)
status_code=cmd_out[0]
output=cmd_out[1]

if status_code==0:
        print("Instance launched successfully")
else:
        print("Something went wrong")

