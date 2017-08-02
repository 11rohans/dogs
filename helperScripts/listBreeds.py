import os


def print_all_breeds():
    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")

    for breed_path in os.listdir(DOG_PATH):
        breed = breed_path.split("-")[1]
        print("<option value=\"" + breed+"\">" + breed + "</option>")


print_all_breeds()
