from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


def AddTask(task):
    global currentTaskCounter
    global Tasks
    Tasks[currentTaskCounter] = task
    currentTaskCounter += 1

def ListTask():
    global currentTaskCounter
    global Tasks
    result = []
    for i in range(currentTaskCounter):
        result.append(Tasks[i])
    return result

###Endpoints###
class Tarefas(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('foo', type = str, required = True,
            help = 'No foo, no service', location = 'json')
        self.reqparse.add_argument('bar', type = str, default = "Oh no, i'm a default value", location = 'json')
        super(Tarefas, self).__init__()

    def get(self):
        global tasks
        return tasks
    def post(self):
        global currentTaskCounter
        global tasks
        args = self.reqparse.parse_args()
        task = {}
        for k, v in args.items():
            if v != None:
                task[k] = v
        currentTaskCounter += 1
        tasks[currentTaskCounter] = task
        return ("ok",200)
        
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
        
        
api.add_resource(Tarefas,'/Tarefas', endpoint = 'Tarefas')
api.add_resource(Tarefa,'/Tarefa/<int:id>', endpoint = 'Tarefa')
api.add_resource(Healthcheck,'/healthcheck', endpoint = 'healthcheck')

currentTaskCounter = 0
tasks = {}

tasks[0] = {"foo" : "foo service is on", "bar" : "chocolate..."}




