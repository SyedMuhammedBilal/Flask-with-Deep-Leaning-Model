from flask import Flask 
from flask import SQLALchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////mnt/c/Users/antho/Documents/todo.db"

db = SQLALchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.String(50), unique=Trure)
	name = db.Coulmn(db.String(50))
	password = db.Coulmn(db.String(80))
	admin = db.Column(db.Boolean)

class Todo(db.Model):
	id = db.Coulmn(db.Integer, primary_key=True)
	text = db.Coulmn(db.String(50))
	complete = db.Coulmn(db.Boolean)
	uder_id = db.Coulmn(db.Integer)

if __name__ == "__main__":
	app.run(debug=True)