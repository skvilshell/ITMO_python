from flask import Flask, request, jsonify, render_template, abort
from double_hash import DoubleHash

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.post('/sum')
def sum():
    """
        Функция суммирования двух чисел
    """
    json = request.get_json()

    if not json or 'x' not in json or 'y' not in json  :
        abort(400)

    response = int(json['x']) + int(json['y'])
    return jsonify(msg = response)

@app.get('/create')
def create():
    n = int(request.args.get('n'))
    table = DoubleHash(n)
    return   jsonify(table = table.get())