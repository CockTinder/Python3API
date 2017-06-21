#!.venv/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"error": True, "msg": "pleas look at api specs on https://github.com/CockTinder/Python3API"})


if __name__ == '__main__':
    app.run(debug=True)
    