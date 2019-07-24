from flask import Flask, Blueprint, request, jsonify, current_app

app2 = Blueprint('app2', __name__)


@app2.route('/')
def hello2():
    return 'Hell222o, World!'