from random import randint

from flask import request, jsonify

from app import app
from app.controller.alpaca_controller import alpaca_controller

@app.route('/')
@app.route('/<age>')
def index(age=None):
    return alpaca_controller.index(age=age)

# TODO: implement profile for each user
@app.route('/profile/<name>')
def profile(name):
    return alpaca_controller.profile(name)

#@app.route('/create', methods=["POST"])
def create():
    data = request.json
    return alpaca_controller.create(data['id'], data['name'], data['displayName'], data['bio'], data['age'], data['hobbies'], data['contact'], data['sex'])
# TODO: implement api

#@app.route('/delete', methods=["POST"])
def delete():
    data = request.json
    return alpaca_controller.delete(data['id'], data['name'], data['displayName'], data['bio'], data['age'], data['hobbies'], data['contact'], data['sex'])
