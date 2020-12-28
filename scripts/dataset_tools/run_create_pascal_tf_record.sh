#!/bin/bash	

# Convert raw PASCAL dataset to TFRecord for object_detection.

# Example usage:
#     python object_detection/dataset_tools/create_pascal_tf_record.py \
#         --data_dir=/home/user/VOCdevkit \
#         --year=VOC2012 \
#         --output_path=/home/user/pascal.record

# flags:

# create_pascal_tf_record.py:
#   --annotations_dir: (Relative) path to annotations directory.
#     (default: 'Annotations')
#   --data_dir: Root directory to raw PASCAL VOC dataset.
#     (default: '')
#   --[no]ignore_difficult_instances: Whether to ignore difficult instances
#     (default: 'false')
#   --label_map_path: Path to label map proto
#     (default: 'data/pascal_label_map.pbtxt')
#   --output_path: Path to output TFRecord
#     (default: '')
#   --set: Convert training set, validation set or merged set.
#     (default: 'train')
#   --year: Desired challenge year.
#     (default: 'VOC2007')

# Try --helpfull to get a list of all flags
python3 create_pascal_tf_record.py \
 --data_dir=/home/sumantra94/Downloads/dataset \
  --year=merged\
  --output_path=/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet_v1/annotations/train/train.record \
  --label_map_path=/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet_v1/annotations/pascal_label_map.pbtxt \
  --set=train_generated