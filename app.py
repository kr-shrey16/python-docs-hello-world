from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! v2 by Kumar Shreyansh Manual change"
