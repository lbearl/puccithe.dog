"""
Routes and views for the flask application.
"""

from datetime import datetime
import flask
import flask.ext.login as flask_login
from puccidog import app, lm
from puccidog.models import User
from puccidog.forms import LoginForm
import os, os.path
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import subprocess

projdir = os.path.dirname(os.path.realpath(__file__))

poochpicsdir = os.path.join(projdir, 'static/poochpics')

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return flask.render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return flask.render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.email

@app.route('/doggiecam')
@flask_login.login_required
def doggiecam():
    """ Renders the doggie cam pages """
    # first up we need to load all of the images from the last day
    # the rpi script will only have the images from the last day, so 
    # basically we just need all of the images in the poochpics dir
    poochpicsfiles = os.listdir(poochpicsdir)
    poochpics = []
    poochpicsfiles.sort(key=lambda x: os.path.getmtime(os.path.join(poochpicsdir, x)))

    for f in reversed(poochpicsfiles):
        poochpics.append(os.path.basename(f))

    return flask.render_template(
        'doggiecam.html',
        poochpics = poochpics,
        title='Doggie Cam',
        year=datetime.now().year
    )



@app.route('/login', methods=['GET', 'POST'])
def login():
  
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        flask_login.login_user(form.user)

        #app.flash('Logged in successfully.')

        return flask.redirect(flask.url_for('home'))

    return flask.render_template('login.html', title='Login', year=datetime.now().year, form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('home'))

@app.route('/14bd03a7947545ca8bf8c048a178721f/update')
def respond_sms():
   response = MessagingResponse()
   process = subprocess.Popen(["/opt/lbearl/bin/c_sms", "-o"], stdout=subprocess.PIPE)
   stdout = process.communicate()[0]
   response.message(stdout.decode('utf-8'))
   return unicode(response)

