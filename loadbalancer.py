from flask import Flask, redirect
from flask_restful import Api, Resource, reqparse
import boto3
import time
import sys
import random
from botocore.exceptions import ClientError

#--- paths

app = Flask(__name__)
api = Api(app)

access_key = sys.argv[1]
secret_key = sys.argv[2]


ec2Resource = boto3.resource('ec2', aws_access_key_id = access_key, aws_secret_access_key = secret_key)

ec2 = boto3.client('ec2')

waiter = ec2.get_waiter('instance_terminated')

#--- Vars

active_instances = {}


###Endpoints###
@app.route('/', defaults={"path":''})
@app.route('/<path:path>')
def catch_all(path):
    if(path == "healthcheck"):
        return ('ok',200)
    
    choice = random.choice(list(active_instances.values()))
    
    if(choice == None):
        return ('error',400)
    newpath = "http://" + choice + ":5000/" + path
    return redirect(newpath, code=302)

#api.add_resource(Tarefa,'/Tarefa/<int:id>', endpoint = 'Tarefa')
#api.add_resource(Healthcheck,'/healthcheck', endpoint = 'healthcheck')

#Run routine

print("I work")

for i in ec2Resource.instances.filter(Filters=[{  
        'Name' : 'instance-state-name', 
        'Values' : ['running']
        }]):
            active_instances[i.id] = i.public_ip_address

print(active_instances)
        


if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=5000)













