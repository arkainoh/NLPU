from flask import Flask
from flaskext.mysql import MySQL
import numpy as np
import json

# references: https://www.slideshare.net/arload/flask-restful-api
# dependency: flask, flask-mysql

global db_host
global db_port
global db_user_name
global db_user_passwd
global db_db
global server_port

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = db_host
app.config['MYSQL_DATABASE_PORT'] = db_port
app.config['MYSQL_DATABASE_USER'] = db_user_name
app.config['MYSQL_DATABASE_PASSWORD'] = db_user_passwd
app.config['MYSQL_DATABASE_DB'] = db_db

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def helloWorld():
  return "HelloWorld"

@app.route("/selectAll", methods=["GET", "POST"])
def selectAll():
  cursor.execute("select * from wv_model")
  rst = cursor.fetchall()
  words = {}
  for i in rst:
    words[i[0]] = json.loads(i[1])
  return json.dumps(words)

@app.route("/upload/<word>", methods=["POST"])
def upload(word):
  cursor.execute("INSERT INTO wv_model (word, vector) VALUES ('" + word + "', '[0,0,0]')")
  conn.commit()
  return "Uploaded"

@app.route("/select/<word>", methods=["GET", "POST"])
def select(word):
  cursor.execute("select * from wv_model where word = '" + word + "'")
  rst = cursor.fetchall()
  words = {}
  for i in rst:
    words[i[0]] = json.loads(i[1])
  return json.dumps(words)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=server_port)

