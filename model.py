from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	"""Users table"""

	__tablename__ = "users"

	email = db.Column(db.String(40), primary_key = True)
	name = db.Column(db.String(40), nullable= False)
	phone_number = db.Column(db.String(20), nullable= False)
	title = db.Column(db.String(40), nullable = False)
	github = db.Column(db.String(60), nullable= False)
	linkedin = db.Column(db.String(80), nullable= False)
	password = db.Column(db.String(80), nullable= False)


class Tech(db.Model):
	"""tech stack"""

	__tablename__ = "techs"

	id = db.Column(db.Integer, nullable= False, primary_key= True)
	tech = db.Column(db.String(40), nullable=False)

class UserTech(db.Model):
	"""users and techs"""

	__tablename__ = "usertechs"

	id = db.Column(db.Integer, nullable= False, primary_key= True)
	email = db.Column(db.String(40), db.ForeignKey('users.email'), nullable=False)
	tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'), nullable= False)


class Company(db.Model):
	"""companies """

	__tablename__ = "companies"

	id = db.Column(db.Integer,primary_key= True, nullable= False)
	name = db.Column(db.String(100), nullable= False)
	location = db.Column(db.String(100), nullable= False)
	website = db.Column(db.String(100), nullable= False) 

class Posting(db.Model):
	"""postings by company's"""

	__tablename__ = "postings"

	id = db.Column(db.Integer, nullable= False, primary_key=True)
	company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
	title = db.Column(db.String(60),nullable= False)
	requirments = db.Column(db.Text, nullable= False)



class PostingTech(db.Model):
	""" postings and tech stack"""
	__tablename__ = "postingstechs"

	id = db.Column(db.Integer,primary_key = True, nullable= False)
	posting_id = db.Column(db.Integer, db.ForeignKey('postings.id'),nullable= False)
	tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'), nullable= False)


def connect_to_db(app):
	"""Connect the database to our Flask app."""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gradtoengdb'
	
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
    
    from server import app
    connect_to_db(app)
    print "Connected to DB."
