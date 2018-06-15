from flask import Flask
#from Flask-RESTful import Resource, Api

app = Flask(__name__)
#api = Api(app)

@app.route("/")
def hello():
    return("hello world")
    