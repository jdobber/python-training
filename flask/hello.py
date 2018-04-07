from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
    	{ "res" : ["Hello World!", "Hello again"] })
