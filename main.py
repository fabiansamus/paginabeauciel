import os 
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g
from flask import session as secion
from sqlalchemy import create_engine, or_, desc, asc
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = 'super_super_secret'
app.debug = True

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from functools import wraps

@app.route('/')
@app.route('/Welcome')
def init():
	return render_template('init.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)