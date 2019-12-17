# -*- coding: utf-8 -*-
"""Region Of Interest Pooling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZgZp0fu5VCZ5_GROPOV7d84rDdX0btuH
"""

import tensorflow as tf
from tensorflow.keras.layers import Layer

# This is a test to implement Region of Interest Pooling
"""
Input is two tensors:
- A batch of images: all images must have the same shape resulting shape
of the tensorf will be (batch_size, img_width img_height, n_channels)
- A batch of Region of Interest proposals: shape of this tensor will be (batch_size, n_rois, 4)

Output:
List of embedding for each image, shape of outputs is (batch_size, num_rois, pool_width, pool_height, n_channels)
"""

from tensorflow.keras.layers import Layer
class ROIPoolingLayer(Layer):
  def __init__(self, pooled_width, pooled_height, **kwargs):
    self.pooled_height = pooled_height
    self.pooled_width = pooled_width
    super(ROIPoolingLayer, self).__init__(**kwargs)
  
  def comput_output_shape(self, input_shape):
    """
    Return the shape of the ROI Layer output
    """
    feature_map_shape, rois_shape = input_shape
    assert feature_map_shape[0] == input_shape[0] # batch size must be the same
    batch_size = feature_map_shape
    num_rois = rois_shape[1]
    num_channels = feature_map_shape[3]
    return (batch_size, num_rois, self.pooled_height, self.pooled_width, num_channels)

  def call(self, x):
    """
    Map the input tensor of the ROI layer to its output

    # Parameters
      x[0] -- Convolutional feature map tensor,
              shape (batch_size, img_width img_height, n_channels)
      x[1] -- Tensor of region of interest from candidate bounding boxes,
              shape (batch_size, n_rois, 4)

    # Output
      pooled_areas -- Tensor with the pooled region of interest
      shape (batch_size, num_rois, pooled_height, pooled_width, n_channels)
    """
    def curried_pool_rois(x):
      return ROIPoolingLayer._pool_rois(x[0], x[1], 
                                        self.pooled_height, 
                                        self.pooled_width)
    pooled_areas = tf.map_fn(curried_pool_rois, x, dtype = tf.float32)
    return pooled_areas
  
  @staticmethod
  def _pool_rois(feature_map, rois, pooled_height, pooled_width):
    """
    Apply ROI pooling to a single image and many region of interest
    """
    def curried_pool_roi(roi):
      return ROIPoolingLayer._pool_roi(feature_map, roi, pooled_height, pooled_width)

    # Use default tensorflow map_fn to map function to each element in rois
    pooled_ares = tf.map_fn(curried_pool_roi, rois, dtype = tf.float32)
    return pooled_ares

  @staticmethod
  def _pool_roi(feature_map, roi, pooled_height, pooled_width):
    """
    Apply ROI pooling to a single image and single region of interest
    """
    # Compute the region of interest
    feature_map_height = int(feature_map.shape[0])
    feature_map_width = int(feature_map.shape[1])

    h_start = tf.cast(feature_map_height * roi[0], 'int32')
    w_start = tf.cast(feature_map_width  * roi[1], 'int32')
    h_end   = tf.cast(feature_map_height * roi[2], 'int32')
    w_end   = tf.cast(feature_map_width  * roi[3], 'int32')

    region = feature_map[h_start: h_end, w_start: w_end]

    # Divide the region into non overlapping areas
    region_height = h_end - h_start
    region_width = w_end - w_start

    h_step = tf.cast(region_height / pooled_height, 'int32')
    w_step = tf.cast(region_width / pooled_width, 'int32')

    # for i in range(pooled_height):
    #   for j in range(pooled_width):
    areas = [[(i* h_step, 
               j* w_step,
               (j + 1)*h_step if i+1 < pooled_height else region_height, 
               (j + 1)*w_step if j+1 < pooled_width else region_width
               )
              for j in range(pooled_width)]
             for i in range(pooled_height)]
    # take the maximum of each area and stack the result
    def pool_area(x):
      return tf.math.reduce_max(region[x[0]:x[2], x[1]:x[3], :], axis = [0, 1])

    pooled_features = tf.stack([[pool_area(x) for x in row] for row in areas])
    return pooled_features

import numpy as np

# Define parameters
batch_size = 1
img_height = 4
img_width = 6
num_channel = 1
num_roi = 2
pooled_width = 2
pooled_height = 2

# Create feature map input
feature_map_shape = (batch_size, img_height, img_width, num_channel)
feature_map_tf = tf.placeholder(tf.float32, shape = feature_map_shape)

feature_map_np = np.asarray([[[[88],[44],[14],[16],[13],[96]],
                     [[61],[63],[15],[120],[66],[15]],
                      [[7],[4],[93],[11],[57],[88]],
                      [[33],[47],[21],[111],[5],[6]]]], dtype = 'float32')
# feature_map_np = np.asarray([[[88,44,14,16,13,96],
#                      [61,63,15,120,66,15],
#                       [7,4,93,11,57,88],
#                       [33,47,21,111,5,6]]], dtype = 'float32')
print(f"feature_map_np shape = {feature_map_np.shape}")

# Create Batch size
roi_tf = tf.placeholder(tf.float32, shape = (batch_size, num_roi, 4))

x_start_1, y_start_1, width_1, height_1 = 0.0, 0.0, 3.0, 3.0
x_start_2, y_start_2, width_2, height_2 = 0.0, 0.0, 6.0, 6.0

roi_np = np.asarray([[[0.0, 0.0, 0.5, 0.5], 
                     [0.0, 0.0, 1.0, 1.0]]], dtype = 'float32')
print("Roi shape = ", roi_np.shape)

# Create layer 
roi_layer = ROIPoolingLayer(pooled_height, pooled_width)
pooled_features = roi_layer([feature_map_tf, roi_tf])
print("Output feature shape: ", pooled_features.shape)

# Run tensorflow session
with tf.Session() as sess:
  result = sess.run(pooled_features, 
                    feed_dict = {feature_map_tf: feature_map_np,
                                 roi_tf:roi_np})
  print("Result shape: ", result.shape)
  print("First roi embedding = ",result[0,0,:,:,0] )
  print("Second roi embedding = ",result[0,1,:,:,0] )