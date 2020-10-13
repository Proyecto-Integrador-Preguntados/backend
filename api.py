# API
import os
import json
import logging
import requests
import pymongo
import json
import flask
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv
from flask_api import status
import random
from jsonschema import validate, ValidationError
from flask import jsonify
load_dotenv()
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
uri = os.getenv("URI_MONGODB")

def question_from_mongo():

    client = pymongo.MongoClient(uri)    
    db = client.get_database()    

    preguntas = db['preguntas']  
    respuesta_preguntas = preguntas.find({}) 
    preguntas_totales = []

    for i in respuesta_preguntas:
        i['_id'] = str(i['_id'])
        preguntas_totales.append(i)
    
    pregunta = random.choice(preguntas_totales)

    return pregunta

class GET_MESSAGE(Resource):

    def post(self):
        response = "OK"
        return response
    
    def get(self):
        response = question_from_mongo()
        return response

api.add_resource(GET_MESSAGE, '/getMessage')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')
