from dogs.cv.bow import Bow
import cv2
import os

sift = cv2.xfeatures2d.SIFT_create()


def train_bow():
    bow = Bow()

    DOG_PATH = os.environ.get("DOG_PATH", "dogs/static/images")
    for breed_path in os.listdir(DOG_PATH):
        for ind_dog in os.listdir(DOG_PATH + "/" + breed_path):
            image_path = DOG_PATH + "/" + breed_path + "/" + ind_dog
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            kp, des = sift.detectAndCompute(image, None)

            bow.train(des)

    bow.save()

    # generate SIFT descriptors for all images

    # train on SIFT descriptors

    # save bow model
