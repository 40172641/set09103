from flask import Flask, redirect, url_for, abort
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World..."

@app.route("/route")
def route():
  return "This is the 'route' route"

@app.route("/goodbye/")
def goodbye():
  return "Goodbye krule world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
