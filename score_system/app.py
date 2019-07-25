from flask import Flask, request, jsonify, current_app
import json
import app2
import services
import dbwork
from flask_cors import CORS
from common import logger
import sys


app = Flask(__name__)
CORS(app)
logger = logger.get_standard_logger('app')

@app.route('/score/sendresult', methods=['POST'])
def send_result():
    json_data = json.loads(request.data)
    return services.send_result_service(json_data)

@app.route('/score/getrankdata', methods=['POST'])
def get_rank_data():
    json_data = json.loads(request.data)
    return services.get_rank_data_service(json_data)

@app.route('/score/checkrestartable/<session_id>', methods=['GET'])
def check_restartable(session_id):
    return services.check_restartable_service(session_id)

@app.route('/score/getuserscore/<session_id>/<user_name>', methods=['GET'])
def get_user_score(session_id, user_name):
    return services.get_user_score_service(session_id, user_name)

@app.route('/score/register_user', methods=['POST'])
def register_user():
    json_data = json.loads(request.data)
    return services.register_user_service(json_data)

@app.route('/score/test', methods=['POST'])
def test():
    json_data = json.loads(request.data)
    return services.test(json_data)


if __name__=='__main__':
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
