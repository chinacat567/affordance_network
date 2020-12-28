####################################################################
## Institute for Infocomm Research, A*STAR
## By Chen Tai Pang, Lawrence
## Dept: Robotics and Automous Systems
## Code: To load a pre-trained model from tensorflow and modify it
## Copyright: 2019, 2020. 
## All rights reserved. 


from __future__ import absolute_import, division, print_function

import tensorflow as tf
# tf.enable_eager_execution() # May not need it anymore. 

from tensorflow import keras
from tensorflow.keras import layers
#  20th Nov, Sumantra : contrib depreceated 
# from tensorflow import contrib
# tfe = contrib.eager

import os

import model_manager

# import tensorflow.contrib.slim as slim


## Load a new mobilenet model from tensorflow.
mobilenet = tf.keras.applications.MobileNet(input_shape = (224,224,4),weights = None, include_top = True)
# mobilenet = tf.keras.applications.MobileNet()

# Check the contents of the network
mobilenet.summary()

# ## You can save the model and weights using a new name. 
# tf.keras.models.save_model(mobilenet, '/home/sumantra94/Documents/Tensorflow/scripts/tensorflow_keras/mobilenetv2_m.h5', save_format = 'h5')
# # model_manager.save_model(model=mobilenet, , json_format=False) # Save the model in h5 with weights.    

# ## Reload the model.
# mobilenetV2_custom = tf.keras.models.load_model("mobilenetv2_m.h5")


# #	remove first two layers
# mobilenetV2_custom._layers.pop() # remove the input layer
# mobilenetV2_custom._layers.pop() # remove the conv padding layer 
# # 	print the model

# #  	save the model 

# #	create new input layers
# new_input_layer = tf.keras.Input(shape =(224,224,4), name = "InputLayer") 
# new_padding_layer = tf.keras.layers.ZeroPadding2D(padding=(255,255)) (new_input_layer)
# # 	create intermediate model
# intermediate_model = mobilenetV2_custom (new_padding_layer)
# main_model = intermediate_model(new_input_layer)


