"""
Author: Sean Coggeshall

Simple Flask web app that serves a greeting message and a route
that prints the message multiple times with iteration numbers.
"""


msg = "Hello from Sean"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello ():
    return msg

@app.route("/pyrev")
def pyrev():
    retval=""
    for i in range (1,14):
        retval = retval + msg + " --> " + str(i) + "</br>"
        if i == 7:
            return (retval)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)