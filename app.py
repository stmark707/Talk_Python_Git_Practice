from flask import Flask
app = Flask(__name__)

@app.route("/") #Video uses a get method but this did not work on our system.
def hello_world():
    return "<p> Hello, World! </p>"