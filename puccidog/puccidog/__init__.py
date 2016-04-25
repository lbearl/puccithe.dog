"""
The flask application package.
"""

from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_TRACK_MODIFICATIONS = True

app = Flask(__name__)
app.secret_key = '2=1$m5B7m1UQ:Mssdlfkjlksdf9sdkfsdl8werjlksdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

import puccidog.views
