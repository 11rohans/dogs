from flask import Flask, render_template
import os
import random


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return ("test")


@app.route("/dog", methods=['GET'])
def get_dog_handler():
    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")

    species_path = random.choice(os.listdir(DOG_PATH))

    dog_image = random.choice(os.listdir(DOG_PATH + "/" + species_path))

    species = species_path.split("-")[1]

    full_path = "images" + "/" + species_path + "/" + dog_image

    return render_template("dog.html", species=species, full_path=full_path)


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
