"""
 Simple API endpoint for returning helloworld
"""
from flask import (Blueprint, render_template, current_app, request,Flask,
                   flash, url_for, redirect, session, abort, jsonify, make_response)

helloworld = Blueprint('helloworld', __name__, url_prefix='/api/helloworld')

@helloworld.route('/helloworld', methods=['GET'])

data = {
     'message' : "helloworld"
   }
   return make_response(jsonify(data))
def index():
   return render_template('index.html')
