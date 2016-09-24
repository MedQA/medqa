# Flask-SQLAlchemy extension instance
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Flask-Login
from flask_login import LoginManager
login_manager = LoginManager()


# Flask-WTF csrf protection
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect()


#Flask-Mail
from flask_mail import Mail, Message
mail = Mail()
