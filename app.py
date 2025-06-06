from flask import Flask, render_template, jsonify

app = Flask(__name__)

USERS = [{
    'id': 1,
    'username': '______',
    'email': '______',
    'password': '_____'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', username=USERS, company_name='AIO')


@app.route("/api/usernames")
def list_users():
  return jsonify(USERS)
#Para datos en formato JSON

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
