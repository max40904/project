# View more python tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tensorflow as tf
from MongoDB import DataCenter 

learning_rate = 0.0003
k_filter = 80
input_layer = 7
training_iters = 1000
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    # stride [1, x_movement, y_movement, 1]
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

# define placeholder for inputs to network
input = tf.placeholder(tf.float32, [None, 19,19,input_layer]) # 28x28
output = tf.placeholder(tf.float32, [None, 225])

## conv1 layer ##

w_conv1 = weight_variable([5,5,input_layer,k_filter])# patch 5 * 5 insize 120 outsize 100
print w_conv1
b_conv1 = bias_variable([k_filter])
print b_conv1
h_conv1 = tf.nn.relu(conv2d(input, w_conv1) + b_conv1)
print h_conv1

w_conv2 = weight_variable([3,3,k_filter,k_filter])
b_conv2 = bias_variable([k_filter])
h_conv2 = tf.nn.relu(conv2d(h_conv1, w_conv2) + b_conv2)
print h_conv2


w_conv3 = weight_variable([3,3,k_filter,k_filter])
b_conv3 = bias_variable([k_filter])
h_conv3 = tf.nn.relu(conv2d(h_conv2, w_conv3) + b_conv3)
print h_conv3

w_conv4 = weight_variable([3,3,k_filter,k_filter])
b_conv4 = bias_variable([k_filter])
h_conv4 = tf.nn.relu(conv2d(h_conv3, w_conv4) + b_conv4)
print h_conv4


w_conv5 = weight_variable([3,3,k_filter,k_filter])
b_conv5 = bias_variable([k_filter])
h_conv5 = tf.nn.relu(conv2d(h_conv4, w_conv5) + b_conv5)
print h_conv5


w_conv6 = weight_variable([3,3,k_filter,k_filter])
b_conv6 = bias_variable([k_filter])
h_conv6 = tf.nn.relu(conv2d(h_conv5, w_conv6) + b_conv6)
print h_conv6

w_conv7 = weight_variable([3,3,k_filter,k_filter])
b_conv7 = bias_variable([k_filter])
h_conv7 = tf.nn.relu(conv2d(h_conv6, w_conv7) + b_conv7)
print h_conv6

w_conv8 = weight_variable([3,3,k_filter,k_filter])
b_conv8 = bias_variable([k_filter])
h_conv8 = tf.nn.relu(conv2d(h_conv7, w_conv8) + b_conv8)
print h_conv8


w_conv9 = weight_variable([3,3,k_filter,k_filter])
b_conv9 = bias_variable([k_filter])
h_conv9 = tf.nn.relu(conv2d(h_conv8, w_conv9) + b_conv9)
print h_conv9


w_conv10 = weight_variable([3,3,k_filter,k_filter])
b_conv10 = bias_variable([k_filter])
h_conv10 = tf.nn.relu(conv2d(h_conv9, w_conv10) + b_conv10)
print h_conv10

w_conv11 = weight_variable([3,3,k_filter,k_filter])
b_conv11 = bias_variable([k_filter])
h_conv11 = tf.nn.relu(conv2d(h_conv10, w_conv11) + b_conv11)
print h_conv11

w_conv12 = weight_variable([1,1,k_filter,1])
b_conv12 = bias_variable([1])
h_conv12=  conv2d(h_conv11, w_conv12) + b_conv12

h_pool13_flat = tf.reshape(h_conv1, [-1 ,15*15*1])
print h_pool13_flat



prediction = tf.nn.softmax(h_pool13_flat)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(output * tf.log(prediction),reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
init = tf.initialize_all_variables()

Data = DataCenter.MongoDB()
saver = tf.train.Saver()
with tf.Session() as sess:
	for step in range(training_iters):
		set_x = Data.SGFReturnSet()
		out_y = Data.SGFReturnAnw()
		cur_color = Data.ReturnColor()
		all_layer_1 = ReturnAllLayer(set_x,cur_color)
		sess.run(optimizer, feed_dict={input: all_layer_1, output: np.reshape(out_y,[1,225]), keep_prob: 1.})
    	if step %100 ==0:
    		print step

# the error between prediction and real data
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
#                                               reduction_indices=[1]))       # loss
# train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# sess = tf.Session()
# # important step
# sess.run(tf.initialize_all_variables())


