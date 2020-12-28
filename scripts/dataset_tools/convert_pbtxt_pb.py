import tensorflow as tf
from google.protobuf import text_format

with open('/home/sumantra94/Documents/Tensorflow/tensorflow_ws/training_demo_ssd_mobilenet/models/ssd_mobilenet_v2/graph.pbtxt') as f:
  txt = f.read()
gdef = text_format.Parse(txt, tf.GraphDef())

tf.train.write_graph(gdef, '/tmp', 'myfile.pb', as_text=False)