from keras.layers import Input, Dense
from keras import backend as K

def _int64_feature(value):
    return K.cast(value, 'float32')
