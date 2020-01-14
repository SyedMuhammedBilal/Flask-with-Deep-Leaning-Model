from flask import Flask, jsonify, request, redirect, render_template
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
from PIL import Image

graph = tf.get_default_graph()

app = Flask(__name__)
modelData = load_model("cats_and_dogs_small_1.h5")

@app.route("/", methods=["POST"])
def index():
	data =request.files
	img = Image.open(data["image"])       #py -m pip install <package name>
	img =image.img_to_array(img)
	img =img.reshape((1,)+img.shape)
	img =img/255
	with graph.as_default():
		prediction = modelData.predict(img)
		if prediction < .5:
			return jsonify({"success": True, "name": "cat"})
		else:
			return jsonify({"success": True, "name": "dog"})
	return jsonify({"success": False}) 

@app.route("/form")
def form():
	return render_template("index.html")



if __name__ == '__main__':
	app.run(debug=True)