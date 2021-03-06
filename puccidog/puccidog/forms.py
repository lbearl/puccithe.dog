from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required
from puccidog.models import User

class LoginForm(Form):
    """The default login form"""

    email = TextField('Email', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            email=self.email.data).first()

        if user is None:
            self.email.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
