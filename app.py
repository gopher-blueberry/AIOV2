from flask import Flask, render_template, jsonify, request
import pymysql
from database import engine, load_users_from_db, add_aplication_to_db
from sqlalchemy import text



app = Flask(__name__)





#Para COMMIT


@app.route("/")
def hello_flask():
  users = load_users_from_db()
  return render_template('home.html', users=users, company_name='AIO')





@app.route("/api/users")
def list_users():
  jobs = load_users_from_db()
  return jsonify(jobs)
#Para datos en formato JSON


@app.route("/user")

def apply_to_be():
   data = request.form
   return render_template('login.html')


    

@app.route("/apply", methods = ['post'])

def apply_to_be_user():
   data = request.form
  #guardar en base
   add_aplication_to_db(data)

   return render_template('application_sub.html', application = data)






if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)






#Este código es para conectarse a la base de datos de Aiven y crear una tabla y luego insertar datos en ella.

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="newdatabaseformysql",
    host= "aio-moviesv2-aio-movies.c.aivencloud.com",
    password="AVNS_5g2Um49Zo1pu6CQWE_S",
    read_timeout=timeout,
    port=13633,
    user="avnadmin",
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()