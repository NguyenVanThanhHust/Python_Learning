from keras.layers import Activation
from keras import backend as K
from keras.utils.generic_utils import get_custom_objects

def elu_activation(x):
	if x > 0 :
		return x
	else :
		alpha = 1.0
		return alpha*(K.exp(x) - 1)
get_custom_objects().update({'custom_activation': Activation(custom_activation)})

model.add(Activation(custom_activation))
		