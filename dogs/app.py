from flask import Flask, render_template, request, make_response
import os
import random


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("score", "0")
    return resp


@app.route("/dog", methods=["GET"])
@app.route("/dog/random", methods=['GET'])
def get_random_dog_handler():
    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")

    breed_path = random.choice(os.listdir(DOG_PATH))

    dog_image = random.choice(os.listdir(DOG_PATH + "/" + breed_path))

    breed = breed_path.split("-")[1].replace("_", " ")

    full_path = "images" + "/" + breed_path + "/" + dog_image

    return render_template(
        "dog.html", breed=breed, full_path=full_path)


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

    # TODO: Convert both of these to lower case (no longer relevant w/ dropdown) # noqa
    # TODO: Alphabetize the dropdown
    # guess = request.form['guess']
    breed = request.form['breed']
    full_path = request.form['full_path']
    guess = request.form['dropdown']
    score = int(request.cookies.get("score"))

    if breed == guess:
        score += 1

    resp = make_response(render_template("guess.html", guess=guess,
                                         breed=breed, full_path=full_path,
                                         score=score))
    resp.set_cookie("score", str(score))

    return resp


# TODO
@app.route("/upload", methods=["GET", "POST"])
def upload_handler():
    pass


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
