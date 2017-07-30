from keras.applications.inception_v3 import InceptionV3
# from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K


K.clear_session()

# Set the number of classes for the final layer
CLASS_NUM = 120

inception = InceptionV3(
    include_top=False, weights='imagenet')

# add a global spatial average pooling layer
x = inception.output
x = GlobalAveragePooling2D()(x)

# fully-connected layer, relu
x = Dense(1024, activation='relu')(x)

# final layer fully connected, logistic
predictions = Dense(CLASS_NUM, activation='softmax')(x)

model = Model(inputs=inception.input, outputs=predictions)

# train only the top layers
for layer in inception.layers:
    layer.trainable = False

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# at this point, we need a python generator to fit the module to
