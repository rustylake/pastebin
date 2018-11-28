from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy(app)
# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'MySQLdb'
USERNAME = 'root'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'User'
a = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = a
SQLALCHEMY_TRACK_MODIFICATIONS = False
