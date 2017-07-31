import os 
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, json
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

@app.route('/signUp')
def signUp():
    return render_template('singup.html')AV

@app.route('/')
def init():
	return render_template('init.html')

@app.route('/Welcome')
def test():
	return render_template('descripcion.html')

@app.route('/formulario')
def formulario():
	return render_template('formulario.html')

@app.route("/add_user", methods=['GET'])
def add_user():
	a = request.args.get('a')
	b= request.args.get('b')
	print(a,b)
	return jsonify("true")

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)