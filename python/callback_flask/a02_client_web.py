import requests
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

API = 'http://localhost:5000'
SELF = 'http://localhost:5001'

task_ids = []
statuses = {}

@app.route('/', methods=['GET'])
def index():
    # for tid in task_ids:
    #     statuses[tid] = requests.get(f"{API}/task/{tid}").json()
    tasks = [(tid, statuses[tid]['status'], statuses[tid]['result']) for tid in task_ids]
    return render_template('index.html', tasks=tasks)



@app.route('/submit', methods=['POST'])
def submit():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    callback_url = f"{SELF}/callback"
    res = requests.post(f"{API}/task", json={'n1': n1, 'n2': n2, 'callback_url': callback_url})
    data = res.json()

    task_ids.append(data['task_id'])
    statuses[data['task_id']] = data

    return redirect('/')

@app.route('/callback', methods=['POST'])
def callback():
    data = request.get_json()
    statuses[data['task_id']] = data
    return "", 204


if __name__ == '__main__':
    app.run(port=5001, debug=True)
