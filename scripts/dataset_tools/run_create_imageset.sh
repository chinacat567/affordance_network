#!/bin/bash
python3 create_imagesets.py \
 -x /home/sumantra94/Downloads/dataset/I2R_Data/Annotations \
 -train 70 \
 -val 20 \
 -test 10 \
 -o_train /home/sumantra94/Downloads/dataset/I2R_Data/ImageSets/Main/train.txt \
 -o_val /home/sumantra94/Downloads/dataset/I2R_Data/ImageSets/Main/val.txt \
 -o_test /home/sumantra94/Downloads/dataset/I2R_Data/ImageSets/Main/test.txt