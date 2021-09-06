from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, Float, MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
# from pybigquery.api import ApiClient



app = Flask(__name__)
CORS(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://hxdmtpmd:P4VTFLD0pt7gGQrWXcUYwM8BGFVnoTOY@arjuna.db.elephantsql.com/hxdmtpmd"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://hxdmtpmd:P4VTFLD0pt7gGQrWXcUYwM8BGFVnoTOY@arjuna.db.elephantsql.com/hxdmtpmd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'