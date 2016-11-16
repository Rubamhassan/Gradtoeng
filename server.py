from model import connect_to_db, db, User, Tech, UserTech
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
import json
app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage"""

	return render_template("homepage.html")

@app.route('/engineerlogin', methods= ['Get'])
def login():
	"""allow the user to get to login page"""
	return render_template("engineerlogin.html")

@app.route('/companylogin', methods= ['Get'])
def comp_login():
	"""allows companies to log in"""
	return render_template("companylogin.html")



if __name__ == "__main__":
	
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0')