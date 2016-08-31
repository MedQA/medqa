from flask.ext.script import Manager, Shell, Server
from flask import current_app
from app import create_app
from app.extensions import db
from app.config import DefaultConfig
import os

def create_my_app(config=DefaultConfig):
    return create_app(config)

manager = Manager(create_my_app)

# runs Flask development server locally at port 5000
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))

# start a Python shell with contexts of the Flask application

@manager.command
def initdb():
    db.drop_all(bind=None)
    db.create_all(bind=None)

if __name__ == "__main__":
    manager.run()
