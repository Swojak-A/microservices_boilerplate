#!/usr/bin/env python
# project/__init__.py

import os
from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

# config
app_settings = os.getenv('APP_SETTINGS', 'project.config.DevelopmentConfig')
print(app_settings)
app.config.from_object(app_settings)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })