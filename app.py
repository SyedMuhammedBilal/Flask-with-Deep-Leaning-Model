from flask import Flask 
from flask import SQLALchemy

app = Flask(__name__)



if __name__ == "__main__":
	app.run(debug=True)