import tensorflow as tf
from tensorflow.python.platform import gfile
with tf.Session() as sess:
    model_filename ='emotion_model.pb'
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        g_in = tf.import_graph_def(graph_def)
LOGDIR='E:\model'
train_writer = tf.summary.FileWriter(LOGDIR)
train_writer.add_graph(sess.graph)

with tf.Session() as sess:
    print("ok1")
    softmax_tensor = sess.graph.get_tensor_by_name('import/predictions/Softmax:0')
    print("ok2")
    #softmax_tensor = sess.graph.get_tensor_by_name('predictions/Softmax:0')