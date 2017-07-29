# Dogs
Simple flask app that uses a CNN to classify dogs by breed

# TODO

### Saturday

Preprocess dog data.
Reading on which Keras pretrained model to use (probably VGG16, VGG19 or InceptionV3).
Write requisite code to set up the model
Train model on dog dataset
DOCUMENTATION

### Sunday
Run predictions to sanity check things
Write a simple benchmarking tool
If time permitting, attempt the other pretrained models and benchmark them against each other

Build a flask interface for uploading images and outputting a prediction

### Monday

Front-end
Deployment considerations

### Beyond

Benchmark other pretrained models if haven't already
Curate/scrape more dog data to improve accuracy


# References

### Dataset

Dataset used is the Stanford Dogs Dataset. It contains "images of 120 breeds of dogs from around the world". This Dataset was the largest publically available dataset for this task, and as such was the natural choice.

http://vision.stanford.edu/aditya86/ImageNetDogs/

Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.
