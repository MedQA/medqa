"""
 Simple API endpoint for returning helloworld

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, make_response)

helloworld = Blueprint('helloworld', __name__)

@helloworld.route('/', methods=['GET'])
#@login_required
def index():
   return render_template('index.html')

"""
