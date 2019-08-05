from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/data")
def hello():
	return jsonify(
            { "res" : [
    		{ "title" : "Bildungsherberge", "gps" : [51.363905,7.502385]},
   			{ "title" : "Fernuni", "gps": [51.377105, 7.493587] },
    		{ "title" : "Pizzeria Italia", "gps" : [51.363504, 7.506455]},
  		  	{ "title" : "Hbf Hagen", "gps" : [51.362393, 7.462261]}
		]})


