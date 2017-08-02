from flask import Flask, render_template, request
import os
import random


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return ("test")


@app.route("/dog", methods=["GET"])
@app.route("/dog/random", methods=['GET'])
def get_random_dog_handler():
    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")

    breed_path = random.choice(os.listdir(DOG_PATH))

    dog_image = random.choice(os.listdir(DOG_PATH + "/" + breed_path))

    breed = breed_path.split("-")[1].replace("_", " ")

    full_path = "images" + "/" + breed_path + "/" + dog_image

    def test():
        print("TESTING")
        return "TEST"

    return render_template(
        "dog.html", breed=breed, full_path=full_path, test=test)


@app.route("/dog/<breed>/<dog_id>", methods=["GET"])
def get_dog_handler(breed, dog_id):
    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")

    breeds = os.listdir(DOG_PATH)
    breed_path = [
        breed_path for breed_path in breeds if breed in breed_path][0]
    breed = breed_path.split("-")[1].replace("_", " ")

    dog_images = os.listdir(DOG_PATH + "/" + breed_path)

    dog_path = [dog_path for dog_path in dog_images if dog_id in dog_path][0]

    full_path = "images" + "/" + breed_path + "/" + dog_path

    return render_template("dog.html", breed=breed, full_path=full_path)


@app.route("/guess/", methods=["POST"])
def guess_handler():
    guess = request.form['guess']
    breed = request.form['breed']
    full_path = request.form['full_path']

    return render_template(
        "guess.html", guess=guess, breed=breed, full_path=full_path)


# TODO
@app.route("/upload", methods=["GET", "POST"])
def upload_handler():
    pass


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
