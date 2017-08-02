# Dogs
Simple flask app that uses a CNN to classify dogs by breed

# Flask stuff/guessing game

### Step 1
Build out a basic guessing game functionality

### Step 2
Build navigational controls so the game can be repeated
Create a good way for the user to know what their options for guessing are
Sanitize user input

### Step 3
Computer vs Human model (Requires CV or DL model)
Score tracking

# TODO Computer Vision (CV) model

### Step 1 (BoF)

Build out a BoF model using a standard dictionary of features
Use a IDF to test for similarity
Generate a list of closest matches and display

### Step 2 (VLAD)

Build out the VLAD representation for features
Use ADC model to test for similarity
Generate a list of closest matches and display

### Beyond

Benchmarking, PCA?

# TODO Deep Learning (DL) Model

### Week 1

Preprocess dog data.
Reading on which Keras pretrained model to use (probably VGG16, VGG19 or InceptionV3).
Write requisite code to set up the model
Train model on dog dataset
DOCUMENTATION

### Week 2
Run predictions to sanity check things
Write a simple benchmarking tool
If time permitting, attempt the other pretrained models and benchmark them against each other

Build a flask interface for uploading images and outputting a prediction

### Week 3

Front-end
Deployment considerations

### Beyond

Benchmark other pretrained models if haven't already
Curate/scrape more dog data to improve accuracy

Do a guess the dog game for users. Machine vs the user.

# How to use

## Guessing game
Start at endpoint /dog to get a random dog.

Guess what breed the dog is and click submit.

# References

### Dataset

Dataset used is the Stanford Dogs Dataset. It contains "images of 120 breeds of dogs from around the world". This Dataset was the largest publically available dataset for this task, and as such was the natural choice.

http://vision.stanford.edu/aditya86/ImageNetDogs/

Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.
