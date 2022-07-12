from cgitb import text
from email import message
from re import template
import re
# from flask_cors import CORS
from urllib import response
from flask import Flask, render_template, request, jsonify
from chat import get_response

from flask import Flask

app = Flask(__name__)
# CORS(app)

@app.route("/")
# @app.get("/")
# def hello_world():
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if the text is valid
    response = get_response(text)
    message = {"answer" : response}
    return jsonify(message)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, port= 8000)