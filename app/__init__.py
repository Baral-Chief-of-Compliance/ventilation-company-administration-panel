from flask import Flask
from config import Config
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)


from app import routes, stored_procedure