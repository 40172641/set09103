from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/private/")
def private():
  # Test for user logged in failed
  # Sp redirect to url login
  return redirect(url_for('login'))

@app.route('/login')
def login():
  return "Please input the user name and password"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


