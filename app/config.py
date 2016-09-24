import os
from common.constants import INSTANCE_FOLDER_PATH


class BaseConfig(object):

   PROJECT = "app"

   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

   DEBUG = False
   TESTING = False

   ADMINS = ['youremail@yourdomain.com']

   # http://flask.pocoo.org/docs/quickstart/#sessions
   SECRET_KEY = os.environ['SECRET_KEY']

class DefaultConfig(BaseConfig):

   # Statement for enabling the development environment
   DEBUG = True

   # Secret key for signing cookies
   SECRET_KEY = os.environ['SECRET_KEY']

   SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
   SQLALCHEMY_TRACK_MODIFICATIONS = True
   #flask_mail
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 465
   MAIL_USERNAME = 'medqadevelop@gmail.com'
   MAIL_PASSWORD = os.environ['EMAIL_KEY']
   MAIL_USE_TLS = False
   MAIL_USE_SSL = True


class LocalConfig(DefaultConfig):
   # config for local development
   pass

class StagingConfig(DefaultConfig):
    # config for staging environment
    pass

class ProdConfig(DefaultConfig):
    # config for production environment
    pass

def get_config(MODE):
   SWITCH = {
      'LOCAL'     : LocalConfig,
      'STAGING'   : StagingConfig,
      'PRODUCTION': ProdConfig
   }
   return SWITCH[MODE]
