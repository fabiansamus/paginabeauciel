import sys

from sqlalchemy import *

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	last_name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	fecha_nacimiento = Column(Date, default=func.now())
	telefono = Column(Integer, nullable=False)
	celular =Column(Integer,nullable=False)
	genero = Column(String(12),nullable=False)
	tipo_identificacion = Column(String(8), nullable=True)
	identificacion = Column(String(11), nullable=False)
	direccion =Column(String(250), nullable=False)


class Ficha(Base):
	__tablename__ = 'Ficha'

	id = Column(Integer,ForeignKey(User.id), primary_key=True)
	tipo_sangre = Column(String(2), nullable=False)
	peso = Column(String(20), nullable=False)
	notas = Column(String(250), nullable=False)

class Trabajo(Base):
	__tablename__ = 'Trabajo'

	id = Column(Integer, primary_key=True)
	tipo = Column(String(250), nullable=False)
	duracion_secion = Column(String(250), nullable=False)
	seciones = Column(String(250), nullable=False)
	fecha_inicio = Column(Date, default=func.now())
	precio = Column(Integer, nullable=False)
	nombre = Column(String(250), nullable=False)

class Secion(Base):
	__tablename__ = 'Secion'

	id = Column(Integer, primary_key=True)
	fecha = Column(String,nullable=False)
	hora = Column(Integer,nullable=False)
	estado = Column(String, nullable=False)# cancelado/vigente/echo/
	id_persona = Column(Integer, ForeignKey(User.id))
	id_tabajo = Column(Integer, ForeignKey(Trabajo.id))

class Ficha_secino(Base):
	__tablename__ = 'Ficha_secion'

	id = Column(Integer,primary_key=True)
	nota = Column(String(600))
	seciones_restantes = Column(Integer)
	numero_secion= Column(Integer)
	id_persona = Column(Integer, ForeignKey(User.id))
	id_tabajo = Column(Integer, ForeignKey(Trabajo.id))
	id_secion = Column(Integer, ForeignKey(Secion.id))

class Precio_trabajo(Base):
	__tablename__ = 'Precio_trabajo'

	id = Column(Integer,primary_key=True)
	precio_trabajo=Column(Integer,nullable=False)
	id_persona = Column(Integer, ForeignKey(User.id))
	id_tabajo = Column(Integer, ForeignKey(Trabajo.id))

class Deposito(Base):
	__tablename__ = 'Deposito'

	id = Column(Integer, primary_key=True)
	total = Column(Integer,nullable=False)
	abono = Column(Integer, nullable=False)
	pendiente = Column(Integer,nullable=False)
	notas = Column(String(250), nullable=False)
	id_persona = Column(Integer, ForeignKey(User.id))
	id_secion = Column(Integer, ForeignKey(Secion.id))

class Admin(Base):
	__tablename__ = "admin"

	id = Column(Integer, primary_key=True)
	a_name = Column(String(30), nullable=False)
	a_password = Column(String(),nullable=False) 

engine = create_engine('sqlite:///beauciel.db')


Base.metadata.create_all(engine)