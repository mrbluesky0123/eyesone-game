from flask import Flask, request, jsonify, current_app
import json
import app2
import services
import dbwork
from common import logger

app = Flask(__name__)
logger = logger.get_standard_logger('app')

@app.route('/score/sendresult', methods=['POST'])
def send_result():
    json_data = json.loads(request.data)
    return services.send_result_service(json_data)

@app.route('/score/checkrestartable/<session_id>/<user_name>', methods=['GET'])
def check_restartable(session_id, user_name):
    return services.check_restartable_service(session_id, user_name)

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
    app.run('0.0.0.0')
