from flask import json

from config.config import ConfigDB
from utils.utils import *

database = ConfigDB()
utils = Utils()


class ControllerUser:
    def save(self, req):
        user = req.get_json()
        if user['name'] == "":
            return json.dumps({"code": 400, "description": "O campo nome é obrigatório!", }), 400
        elif len(user['name']) > 150:
            return json.dumps({"code": 400, "description": "Nome não pode utrapassar 150 caracteres!", }), 400
        elif user['cpf'] == "":
            return json.dumps({"code": 400, "description": "O campo cpf é obrigatório!", }), 400
        elif user['email'] == "":
            return json.dumps({"code": 400, "description": "O campo e-mail é obrigatório!", }), 400
        elif len(user['email']) > 400:
            return json.dumps({"code": 400, "description": "E-mail não pode utrapassar 400 caracteres!", }), 400
        elif user['cpf'] != "":
            response = utils.validar_cpf(user['cpf'])
            if response == False:
                return json.dumps({"code": 400, "description": "CPF invalido!", }), 400
            else:
                if user['email'] != "":
                    responseEmail = utils.validar_email(user['email'])
                    if responseEmail == False:
                        return json.dumps({"code": 400, "description": "Email invalido!", }), 400
                    else:
                        return database.save(user)

    def remove(self, req):
        user = req.get_json()
        if user['cpf'] == None:
            return json.dumps({"code": 400, "description": "CPF invalido!", }), 400
        else:
            return database.delete(user)

    def query(self, req):
        user = req.get_json()
        return database.query(user)


    def queryAll(self, req):
        user = req.get_json()
        return database.queryAll(user)
