#!/bin/bash	
# usage: generate_tfrecord.py [-h] [-x XML_DIR] [-l LABELS_PATH]
#                             [-o OUTPUT_PATH] [-i IMAGE_DIR] [-c CSV_PATH]

# Sample TensorFlow XML-to-TFRecord converter

# optional arguments:
#   -h, --help            show this help message and exit
#   -x XML_DIR, --xml_dir XML_DIR
#                         Path to the folder where the input .xml files are
#                         stored.
#   -l LABELS_PATH, --labels_path LABELS_PATH
#                         Path to the labels (.pbtxt) file.
#   -o OUTPUT_PATH, --output_path OUTPUT_PATH
#                         Path of output TFRecord (.record) file.
#   -i IMAGE_DIR, --image_dir IMAGE_DIR
#                         Path to the folder where the input image files are
#                         stored. Defaults to the same directory as XML_DIR.
#   -c CSV_PATH, --csv_path CSV_PATH
#                         Path of output .csv file. If none provided, then no
#                         file will be written.
python3 generate_tfrecord.py \
 --xml_dir=/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet_v1/images/train \
 --labels_path=/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet_v1/annotations/pascal_label_map.pbtxt \
 --output_path=/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet_v1/annotations/train/train.record