from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email

		def __repr__(self):
			return '<User %r>' % self.username


def create_users():
	admn = User('admin', 'anbu23477@gmail.com')
	user = User('vova', 'vova_cons@live.com')
	db.session.add(admin)
	db.session.add(user)
	db.session.commit()


@app.route("/", methods=["POST"])
def addUser():
	db.create_all()
	username = request.form["name"]
	email = request.form["email"]
	user = User(username, email)
	db.session.add(user)
	params = {"text" : "Succesful"}
	return render_template("report.html", **params)

@app.route("/", methods= ["GET"])
def getUsers():
	db.create_all()
	user = User.query.first()
	return render_template("index.html", user=user)

	#db.create_all()
	#if (request.method == "POST"):
	#else:
	#	create_users()
	#user = User.query.filter_by(username='admin').first()
	#if (user == None):
	#	user = User('username', 'example@mail.com')
	#params = { "id" : "Hello world!!!!!!!", "name" : "asjhd"}
	#return render_template("index.html", **params)


if __name__ == "__main__":
	app.run()