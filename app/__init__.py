from flask import Flask, jsonify, request, current_app
from flask_cors import CORS
from config import Config
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime, timedelta
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)
jwt = JWTManager(app)


from app import routes, stored_procedure, hash, geo
