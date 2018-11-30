#!/usr/bin/env python3
import sys
import json
import requests as r

def test_health():
    return r.get("http://127.0.0.1:5000/healthcheck")

def adicionar():
    print("--- Adicionando tarefa")
    values = map(str, sys.argv[2].strip('[]').split(','))
    foo = values[0]
    bar = values[1]
    response = r.post("http://127.0.0.1:5000/Tarefas", json = {"foo" : foo, "bar" : bar}).json()
    if(response != "ok"):
        print("Error: ", response)
    else:
        print("adicionado com sucesso")


def listar():
    print("---- Lista de tarefas ----")
    response = r.get("http://127.0.0.1:5000/Tarefas").json()
    for i in response.keys():
        entry = " -Tarefa " + i + "--> "
        for k in response[i].keys():
            entry += (k + " : " + response[i][k] + " | ")
            
        print(entry)
        
def buscar():
    iden = sys.argv[2]
    print("--- Procurando por tarefa com id ", iden)
    response = r.get("http://127.0.0.1:5000/Tarefas").json()
    if (not (iden in response.keys())):
        print("Id inexistente")
        return 0
    else:
        entry = " -Tarefa " + iden + "--> "
        for k in response[iden].keys():
            entry += (k + " : " + response[iden][k] + " | ")
            
        print(entry)
        return entry

def apagar():
    iden = sys.argv[2]
    print("--- Apagando por tarefa com id ", iden)
    response = r.delete("http://127.0.0.1:5000/Tarefa/" + iden).json()
    if(response != None):
        print("Nao foi possivel deletar, confira o Healthcheck e o Id")
    else:
        print("Deletado")

def atualizar():
    print("--- Atualizando tarefa")
    iden = sys.argv[2]
    values = map(str, sys.argv[3].strip('[]').split(','))
    foo = values[0]
    bar = values[1]
    print(values)
    response = r.put("http://127.0.0.1:5000/Tarefa/" + iden, json = {"foo" : foo, "bar" : bar}).json()
    print(response)
    if(response != "ok"):
        print("Error: ", response)
    else:
        print("Atualizado com sucesso")



###Run###
userkey = sys.argv[1]

funcs = {"adicionar" : adicionar,
          "listar" : listar,
          "buscar" : buscar,
          "apagar" : apagar,
          "atualizar" : atualizar,
          }

if(not (userkey in funcs)):
    print("Comando invalido")
else:
    funcs[userkey]()
