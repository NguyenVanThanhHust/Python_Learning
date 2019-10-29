import tensorflow as tf
from tensorflow.python.platform import gfile
GRAPH_PB_PATH = 'emotion_model.pb'
GRAPH_PB_PATH2 = 'dogs_breed_classification/trained_model/retrained_graph.pb'
with tf.Session() as sess:
   print("load graph")
   with gfile.FastGFile(GRAPH_PB_PATH,'rb') as f:
      graph_def = tf.GraphDef()
   graph_def.ParseFromString(f.read())
   sess.graph.as_default()
   tf.import_graph_def(graph_def, name='')
   graph_nodes=[n for n in graph_def.node]
   names = []
   for t in graph_nodes:
      names.append(t.name)
   print(names)
   print(tf.contrib.graph_editor.get_tensors(tf.get_default_graph()))

