from flask.ext.login import UserMixin
from puccidog import lm

class User(UserMixin):
    """The basic user object"""
    pass

    def __init__(self, email=None, password=None):
        self.id = email
        self.password = password

    @lm.user_loader
    def user_loader(email):
        print email
        #user = next(u for u in users if u.id == [email])
        user = users[email].pop()
        if user is None:
            return

        return user

    @lm.request_loader
    def request_loader(request):
        email = request.form.get('email')
        if email not in users:
            return

        user = User()
        user.id = email

        # DO NOT ever store passwords in plaintext and always compare password
        # hashes using constant-time comparison!
        user.is_authenticated = request.form['pw'] == users[email]['pw']

        return user

    def check_password(self, password):
        return self.password == password

users = {"luke@bearl.me": {User("luke@bearl.me", "testpw")}, "gwen.paja@gmail.com": {User("gwen.paja@gmail.com", "test2")}}