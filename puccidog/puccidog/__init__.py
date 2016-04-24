"""
The flask application package.
"""

from flask import Flask
from flask.ext.login import LoginManager


app = Flask(__name__)
app.secret_key = '2=1$m5B7m1UQ:Mssdlfkjlksdf9sdkfsdl8werjlksdf'
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

import puccidog.views
