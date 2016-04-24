"""
Routes and views for the flask application.
"""

from datetime import datetime
import flask
import flask.ext.login as flask_login
from puccidog import app, lm
from puccidog.models import User
from puccidog.forms import LoginForm

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
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return flask.flask.render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/login', methods=['GET', 'POST'])
def login():
  
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        flask_login.login_user(form.user)

        #app.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        #if not next_is_valid(next):
        #    return abort(400)

        flask.session['user_id'] = form.user.id

        return flask.redirect(next or flask.url_for('home'))

    return flask.render_template('login.html', title='Login', year=datetime.now().year, form=form)