from flask import Flask 

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

USERNAME = 'root'
PASSWORD = '12345678'
SERVER = 'localhost'
DB = 'bd'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

db = SQLAlchemy(app)

from .views import cliente_views


