from flask import Flask
import os
import uuid as uuid
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searchengineoptimization.db'
app.config['SECRET_KEY'] = "cairocoders-ednalan"

db = SQLAlchemy(app)

class Keywordplanner(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	keyword = db.Column(db.String(255))
	keyword_suggestions = db.Column(db.Text)
	meta_description = db.Column(db.Text)
	meta_description_suggestions = db.Column(db.Text)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	firstname = db.Column(db.String(200), nullable=False, unique=True)
	lastname = db.Column(db.String(200), nullable=False, unique=True)
	companyname = db.Column(db.String(200), nullable=False)
	companyaddress = db.Column(db.Text(1000), nullable=False)
	email = db.Column(db.String(200), nullable=False)
	password = db.Column(db.String())

	##   postgresql://user:password@database.us-west-2.rds.amazonaws.com:5432/mydatabase   ##