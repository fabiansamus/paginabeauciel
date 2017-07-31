from sqlalchemy import create_engine, or_, desc, asc
from sqlalchemy.orm import sessionmaker
from beauciel_db import Base, User, Ficha, Trabajo, Secion, Ficha_secino, Precio_trabajo, Deposito, Admin

engine = create_engine('sqlite:///beauciel.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Admin = Admin(a_name='fabian',a_password='fabian')
# session.add(Admin)
# session.commit()

def check_admin(user,password):
	admin = session.query(Admin).filter_by(a_name=user,a_password=password).first()
	if admin is None:
		return False
	else:
		return True