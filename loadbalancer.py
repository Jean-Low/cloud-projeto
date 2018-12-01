from flask import Flask
from flask_restful import Api, Resource, reqparse
import boto3
import time
import sys
from botocore.exceptions import ClientError

#--- paths

app = Flask(__name__)
api = Api(app)

access_key = sys.argv[1]
secret_key = sys.argv[2]


ec2Resource = boto3.resource('ec2', aws_access_key_id = access_key. aws_secret_key_id = secret_key)

ec2 = boto3.client('ec2')

waiter = ec2.get_waiter('instance_terminated')

#--- Vars




###Endpoints###
class Tarefa(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('foo', type = str, required = True,
            help = 'No foo, no service', location = 'json')
        self.reqparse.add_argument('bar', type = str, default = "Oh no, i'm a default value", location = 'json')
        super(Tarefa, self).__init__()

    def get(self,id):
        global tasks
        if id in tasks:
            return tasks[id]
        return {"message" : "No task on this ID"}
        
    def put(self,id):
        global tasks
        if not (id in tasks):
            return {"message" : "No task on this ID"}
        task = {}
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v != None:
                task[k] = v
        tasks[id] = task
        return ("ok",200)
        
    def delete(self,id):
        global tasks
        if not (id in tasks):
            return {"message" : "No task on this ID"}
        tasks.pop(id)

class Healthcheck(Resource):
    def get(self):
        return ("",200)
        
        
#Run routine
#api.add_resource(Tarefa,'/Tarefa/<int:id>', endpoint = 'Tarefa')
api.add_resource(Healthcheck,'/healthcheck', endpoint = 'healthcheck')

currentTaskCounter = 0
tasks = {}

tasks[0] = {"foo" : "foo service is on", "bar" : "chocolate..."}


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=5000)



