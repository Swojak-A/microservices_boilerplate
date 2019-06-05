#!/usr/bin/env python
# project/__init__.py

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

# config
app_settings = os.getenv('APP_SETTINGS', 'project.config.DevelopmentConfig')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

from project.models import User


# routes

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
