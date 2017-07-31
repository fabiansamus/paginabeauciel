import os 
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, json
from flask import session as secion
from sqlalchemy import create_engine, or_, desc, asc
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from data import check_admin


app = Flask(__name__)
app.secret_key = 'super_super_secret'
app.debug = True

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from functools import wraps
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in secion:
            return test(*args,**kwargs)
        else:
            flash('log in para accesar a la pagina')
            return redirect(url_for('form'))
    return wrap



@app.route('/signUp')
def signUp():
    return render_template('singup.html')

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

@app.route("/form", methods=['POST'])
def formulario_add():
	user = request.form['first_name']
	last = request.form['last_name']
	gender = request.form['gender']
	type_id = request.form['identification_type']
	id_ = request.form['identification']
	phone = request.form['phone']
	movil = request.form['movil']
	email = request.form['email']
	identificacion = request.form['identification']
	birth = request.form['date_birth']
	address = request.form['address']
	return json.dumps({'status':'OK'})

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    if check_admin(user,password) == True and secion['logged_in'] == False:
    	secion['logged_in']=True
    	secion['user_id']= user.id
    	return json.dumps({'status':'succes'}), redirect(url_for('formulario'))
    else:
    	return json.dumps({'status':'NOT OK','user':user}), redirect(url_for('signUp'))


@app.route("/logout")
@login_required
def logout():
    secion.pop("logged_in")
    secion.pop('user_id')
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)