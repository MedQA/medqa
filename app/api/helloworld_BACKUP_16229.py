"""
 Simple API endpoint for returning helloworld
<<<<<<< HEAD

=======
"""
>>>>>>> 6ff09ad4dbd79c0c6b65d64a3b1282a6619c9d86
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, make_response)

helloworld = Blueprint('helloworld', __name__)

@helloworld.route('/', methods=['GET'])
<<<<<<< HEAD
#@login_required
def index():
   return render_template('index.html')

"""
=======
def index():
   return render_template('index.html')
>>>>>>> 6ff09ad4dbd79c0c6b65d64a3b1282a6619c9d86
