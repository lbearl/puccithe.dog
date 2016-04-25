from flask.ext.login import UserMixin
from puccidog import lm, db
import bcrypt

class User(UserMixin, db.Model):
    """The basic user object"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    @lm.user_loader
    def user_loader(user_id):
        print 'Loading user with email: ' + user_id
        user = User.query.filter_by(
            id=user_id).first()
        if user is None:
            return

        return user

    @lm.request_loader
    def request_loader(request):
        email = request.form.get('email')
        if email is None or email.data is None:
            return
        print 'Loading user with email: ' + email.data
        user = User.query.filter_by(
            email=request.email.data).first()

        # DO NOT ever store passwords in plaintext and always compare password
        # hashes using constant-time comparison!
        user.is_authenticated = True

        return user

    def check_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8')) == self.password