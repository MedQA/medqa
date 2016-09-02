from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, login_manager
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(70),nullable=False, unique=True, index=True)
    password_hash = db.Column('password',db.String(), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(7), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    blood_grp = db.Column(db.String(5),nullable=True, default='')
    location = db.Column(db.String(128),nullable=True, default='')
    allergies = db.Column(db.String(500), nullable=True, default='')
    medical_ailments = db.Column(db.String(500), nullable=True, default='')
    previous_medications = db.Column(db.String(500), nullable=True, default='')

    def _get_password(self):
        return self.password_hash

    def _set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Hide password encryption by exposing password field only.
    password = db.synonym('password_hash',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # methods
    @classmethod
    def authenticate(cls, email, password):
        user = User.query.filter(db.or_(User.email == email)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def is_email_taken(cls, email_address):
        return db.session.query(db.exists().where(User.email==email_address)).scalar()

    def get_token(self, expiration=100):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'user':self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        id = data.get('user')
        if id:
            return User.query.get(id)
        return None
