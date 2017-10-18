from flask import Flask, request
app = Flask(__name__)

@app.route("/hello/")
def hello():
  name = request.args.get('name', '')
  city = request.args.get('city', '')
  if name == '' or city == '':
    return "no params supplied"
  else:
    return "Hello %s" % name and "City %s" % city
  

@app.route("/example/")
def example():
  city = request.args.get('city', '')
  if city == '':
    return "No parameters supplied"
  else:
    return "City %s" % city

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
