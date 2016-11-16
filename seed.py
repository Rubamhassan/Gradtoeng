from model import connect_to_db, db, User, Tech, UserTech, Company, Posting, PostingTech

from server import app

connect_to_db(app)

db.drop_all()

db.create_all()

def load_users():
	"""load users into database"""
	with open('./seed_data/user.tsv','r+') as data:
		for i, row in enumerate(data):
			row = row.rstrip()
			print row 
			email, name, phone_number, title, github, linkedin, password = row.split ("\t")

			users = User(
				email= email,
				name = name,
				phone_number = phone_number,
				title = title,
				github = github,
				linkedin = linkedin,
				password = password)

			db.session.add(users)
			db.session.commit()


if __name__ == '__main__':
	load_users()
