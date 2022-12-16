from time import time
from flask import Blueprint

time_api = Blueprint('time_api', __name__)

@time_api.route('/get_time', methods=["GET"])
def get_current_time():
    return {'time': time()}