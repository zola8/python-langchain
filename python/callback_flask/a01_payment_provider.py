import random
import threading
import time
from uuid import uuid4

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}


def process(task_id, n1, n2, callback_url):
    time.sleep(random.randint(5, 15))
    try:
        result = n1 / n2
        tasks[task_id] = {'status': 'SUCCESS', 'result': result }
    except ZeroDivisionError:
        tasks[task_id] = {'status': 'FAILED', 'result': None }

    time.sleep(2)

    if callback_url:
        try:
            res = requests.post(callback_url, json={'task_id': task_id, **tasks[task_id]})
            print(res.json())
        except requests.exceptions.RequestException as e:
            print(e)


@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    n1 = data['n1']
    n2 = data['n2']
    callback_url = data.get('callback_url')
    task_id = str(uuid4())
    tasks[task_id] = {'status': 'PROCESSING', 'result': None }

    threading.Thread(target=process, args=(task_id, n1, n2, callback_url)).start()
    return jsonify({'task_id': task_id, **tasks[task_id]}), 202


@app.route('/task/<task_id>', methods=['GET'])
def get_task(task_id):
    time.sleep(2)
    task = tasks.get(task_id)

    if not task:
        return jsonify({'error': 'not found'}), 404

    return jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)

