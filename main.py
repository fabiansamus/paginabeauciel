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
def init():
	return render_template('init.html')

@app.route('/Welcome')
def test():
	return render_template('descripcion.html')

@app.route('/formulario')
def formulario():
	return render_template('formulario.html')

@app.route("/add_user", methods=['POST'])
def add_user():
	print("en en tro en el perimetro")
	my_data = request.form['mydata']
	return jsonify("true")

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/add')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)