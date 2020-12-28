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
mobilenet = tf.keras.applications.MobileNetV2()

## Check the contents of the network
mobilenet.summary()

## You can save the model and weights using a new name. 
tf.keras.models.save_model(mobilenet, '/home/sumantra94/Documents/Tensorflow/scripts/tensorflow_keras/mobilenetv2_m.h5', save_format = 'h5')
# model_manager.save_model(model=mobilenet, , json_format=False) # Save the model in h5 with weights.    

## Reload the model.
mobilenetV2_custom = tf.keras.models.load_model("mobilenetv2_m.h5")

mobilenetV2_custom._layers.pop(-1) # remove the last layer

# Get the last layer
new_last_layer = mobilenetV2_custom.layers[-1]

# print the contents of the last layer. 
print("new_last_layer = {}, shape  = {}".format(new_last_layer.name,new_last_layer.output_shape))

intermediate_layer_model = tf.keras.Model(inputs=mobilenetV2_custom.input,
                                 outputs=mobilenetV2_custom.get_layer("global_average_pooling2d").output,name="IntermediateModel")

# Check the newly revised
intermediate_layer_model.summary()
#mobilenetV2_custom.summary()
 

### Sample 1) to create a new model using the above modified model: 
### Sumantra: May not work with the latest version of the Tensorflow. Please check. 
# img_input = tf.keras.Input(shape=(224, 224, 3), name='mn_v2')
# #intermediate_layers = mobilenetV2_custom(img_input)
# #img_input = keras.Input(shape=(28, 28, 1), name='img')
# x = layers.Conv2D(16, 3, activation='relu')(img_input)
# x = layers.Conv2D(32, 3, activation='relu')(x)
# x = layers.MaxPooling2D(3)(x)
# x = layers.Conv2D(32, 3, activation='relu')(x)
# x = layers.Conv2D(16, 3, activation='relu')(x)
# intermediate_layers = layers.GlobalMaxPooling2D()(x)

# new_model1 = tf.keras.Model(img_input, intermediate_layers, name='MobileNetV2_modified')

# new_model1.summary()


## Sample 2) to create a new model using the above modified model:
print("mobilenetV2_custom output = {}".format(mobilenetV2_custom.output))

new_input2_input = keras.Input(shape=(1280,), name='encoded_img')
x1 = tf.keras.layers.Dense(2048, activation='relu',name="layer2")(new_input2_input)
final_output = tf.keras.layers.Dense(2, activation='relu',name="layer3")(x1)
new_model2 = tf.keras.Model(new_input2_input, final_output,name='model2')
new_model2.summary()

main_input = tf.keras.Input(shape=(224, 224, 3), name='main_input')
x_model1 = intermediate_layer_model(main_input)#mobilenetV2_custom(main_input)
x_model2 = new_model2(x_model1)
main_model = tf.keras.Model(main_input,x_model2,name="main_model")

main_model.summary()

# Save the newly created model

# model_manager.save_model(model=main_model, filename_without_ext="mobilenetv2_m2", json_format=False)
tf.keras.models.save_model(main_model, '/home/sumantra94/Documents/Tensorflow/scripts/tensorflow_keras/mobilenetv2_m2.h5', save_format = 'h5')


# Reload the newly created model 
model_new_MobileNetV2 = tf.keras.models.load_model("mobilenetv2_m2.h5")

model_new_MobileNetV2.summary()

# Plot the model
# Sumantra: Please check the following function whether it is work in the latest Tensorflow.
keras.utils.plot_model(model_new_MobileNetV2, 'model_new_MobileNetV2.png', show_shapes=True)

# Note: Inside a Keras model, each layer can be either a model or a layer. 
# If the layer encapsulates a model inside, you can treat this layer as model (which consists of
# multiple layers inside).  
model_new_MobileNetV2.layers[1].summary() # retrieve the summary of the model stored inside layer 1. 

keras.utils.plot_model(model_new_MobileNetV2.layers[1], 'model_new_MobileNetV2_l1_M.png', show_shapes=True)


#new_model.compile(loss='mean_squared_error', optimizer='sgd') # No error here

#new_model2.build(input_shape=(224, 224, 3))


# encoder_input = keras.Input(shape=(28, 28, 1), name='original_img')
# x = layers.Conv2D(16, 3, activation='relu')(encoder_input)
# x = layers.Conv2D(32, 3, activation='relu')(x)
# x = layers.MaxPooling2D(3)(x)
# x = layers.Conv2D(32, 3, activation='relu')(x)
# x = layers.Conv2D(16, 3, activation='relu')(x)
# encoder_output = layers.GlobalMaxPooling2D()(x)

# encoder = keras.Model(encoder_input, encoder_output, name='encoder')
# encoder.summary()

# decoder_input = keras.Input(shape=(16,), name='encoded_img')
# x = layers.Reshape((4, 4, 1))(decoder_input)
# x = layers.Conv2DTranspose(16, 3, activation='relu')(x)
# x = layers.Conv2DTranspose(32, 3, activation='relu')(x)
# x = layers.UpSampling2D(3)(x)
# x = layers.Conv2DTranspose(16, 3, activation='relu')(x)
# decoder_output = layers.Conv2DTranspose(1, 3, activation='relu')(x)

# decoder = keras.Model(decoder_input, decoder_output, name='decoder')
# decoder.summary()

# autoencoder_input = keras.Input(shape=(28, 28, 1), name='img')
# encoded_img = encoder(autoencoder_input)
# decoded_img = decoder(encoded_img)
# autoencoder = keras.Model(autoencoder_input, decoded_img, name='autoencoder')
# autoencoder.summary()



# for layer in mobilenetV2_custom.layers: # just exclude last layer from copying
#     print("\t{}".format(layer))
#     new_net.add(layer)

# For fine tuning, disable the training of those layers
# for layer in mobilenetV2_custom.layers:
#     layer.trainable = False     

# mobilenetV2_custom.add(Dense(2, activation='softmax'))

# new_last_layer = tf.keras.layers.Dense(2,activation=tf.nn.softmax,name="cl_output")


# num_layers = len(mobilenetV2_custom.layers)
# print("\nLayers (no layers = {}):".format(num_layers))

# for i in range(0,num_layers):
#     print("\t{}".format(mobilenetV2_custom.layers[i].name))

# print("\nModel outputs = {}\n".format(mobilenetV2_custom.outputs))   



 
