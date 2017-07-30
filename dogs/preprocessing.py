import scipy.io
from keras.preprocessing.image import ImageDataGenerator

dogs_data_train = scipy.io.loadmat("data/train_data.mat")
dogs_data_test = scipy.io.loadmat("data/test_data.mat")

datagen = ImageDataGenerator(
    featurewise_center=True,
    samplewise_center=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-6,
    rotation_range=0.,
    width_shift_range=0.,
    height_shift_range=0.,
    shear_range=0.,
    zoom_range=0.,
    channel_shift_range=0.,
    fill_mode='nearest',
    cval=0.,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None
)

print(type(dogs_data_train))
