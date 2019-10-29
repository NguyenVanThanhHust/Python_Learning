#Declare model paremeters
batch_size = 100
learing_rate = 0.005
output_every = 5
generations = 500
evaluation_size = 500
crop_height = 24
crop_width = 24
num_channels = 1
image_height = train_xdata[0].shape[0]
image_width = train_xdata[0].shape[1]
target_size = max(train_labels) + 1
conv1_features = 25
conv2_features = 50
max_pool_size1 = 2
max_pool_size2 = 2
fully_connected_size1 = 100