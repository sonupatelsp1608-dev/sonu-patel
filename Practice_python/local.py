# from flask import Flask, jsonify, request
# 
# app = Flask(__name__)
# 
# @app.route("/hello", methods=["GET","POST"])
# def hello():
    # if request.method=="GET":
        # return jsonify({"message": "Hello Sonu"})
    # elif request.method=="POST":
        # return jsonify({"message": "Hello Sonu"})
    # else:
        # return "method not allow"
# app.run(debug=True)
# 

from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

class HelloAPI(MethodView):
    def get(self):
        return jsonify({"message": "Hello Sonu"})
    
    def post(self):
        return jsonify({"message": "Hello Sonu12345"})

# Route bind karna
app.add_url_rule('/hello', view_func=HelloAPI.as_view('hello_api'))

app.run(debug=True)