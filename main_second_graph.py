import tensorflow as tf
from MongoDB import DataCenter
from gameinfo import game
import numpy as np

learning_rate = 0.003
input_stack = 24
k_filter = input_stack * 2
train_iters = 10



def weight_variable(shape,names):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial,name = names)



def bias_variable(shape,names):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name = names)


def conv2d(x, W):
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # stride [1, x_movement, y_movement, 1]
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

with tf.name_scope('input'):
	xs = tf.placeholder(tf.float32, [None, 15,15,input_stack],name='x_input')
	ys = tf.placeholder(tf.float32, [None, 225],name = 'y_input')
with tf.name_scope('layer_1'):
	with tf.name_scope('weight'):
		W_conv1 = weight_variable([5, 5, input_stack, k_filter],'W_conv1')
		tf.histogram_summary('layer_1' + '/weights', W_conv1)
	with tf.name_scope('biases'):
		b_conv1 = bias_variable([k_filter],'b_conv1')
		tf.histogram_summary('layer_1'  + '/biases', b_conv1)
	with tf.name_scope('h_conv1'):
		h_conv1 = tf.nn.relu(conv2d(xs, W_conv1) + b_conv1)
	tf.histogram_summary('layer_1' + '/outputs', h_conv1)

with tf.name_scope('layer_2'):
	with tf.name_scope('weight'):
		W_conv2 = weight_variable([3, 3, k_filter, k_filter],'W_conv2')
		tf.histogram_summary('layer_2' + '/weights', W_conv2)
	with tf.name_scope('biases'):
		b_conv2 = bias_variable([k_filter],'b_conv2')
		tf.histogram_summary('layer_2'  + '/biases', b_conv2)
	with tf.name_scope('h_conv2'):
		h_conv2 = tf.nn.relu(conv2d(h_conv1, W_conv2) + b_conv2)
	tf.histogram_summary('layer_2' + '/outputs', h_conv2)



with tf.name_scope('layer_3'):
	with tf.name_scope('weight'):
		W_conv3 = weight_variable([3, 3, k_filter, k_filter],'W_conv3')
		tf.histogram_summary('layer_3' + '/weights', W_conv3)
	with tf.name_scope('biases'):
		b_conv3 = bias_variable([k_filter],'b_conv3')
		tf.histogram_summary('layer_3'  + '/biases', b_conv3)
	with tf.name_scope('h_conv3'):
		h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3) + b_conv3)
	tf.histogram_summary('layer_3' + '/outputs', h_conv3)


with tf.name_scope('layer_4'):
	with tf.name_scope('weight'):
		W_conv4 = weight_variable([3, 3, k_filter, k_filter],'W_conv4')
		tf.histogram_summary('layer_4' + '/weights', W_conv4)
	with tf.name_scope('biases'):
		b_conv4 = bias_variable([k_filter],'b_conv4')
		tf.histogram_summary('layer_4'  + '/biases', b_conv4)
	with tf.name_scope('h_conv4'):
		h_conv4 = tf.nn.relu(conv2d(h_conv3, W_conv4) + b_conv4)
	tf.histogram_summary('layer_4' + '/outputs', h_conv4)



with tf.name_scope('layer_5'):
	with tf.name_scope('weight'):
		W_conv5 = weight_variable([3, 3, k_filter, k_filter],'W_conv5')
		tf.histogram_summary('layer_5' + '/weights', W_conv5)
	with tf.name_scope('biases'):
		b_conv5 = bias_variable([k_filter],'b_conv5')
		tf.histogram_summary('layer_5'  + '/biases', b_conv5)
	with tf.name_scope('h_conv5'):
		h_conv5 = tf.nn.relu(conv2d(h_conv4, W_conv5) + b_conv5)
	tf.histogram_summary('layer_5' + '/outputs', h_conv5)

with tf.name_scope('layer_6'):
	with tf.name_scope('weight'):
		W_conv6 = weight_variable([1, 1, k_filter, 1],'W_conv6')
		tf.histogram_summary('layer_6' + '/weights', W_conv6)
	with tf.name_scope('biases'):
		b_conv6 = bias_variable([1],'b_conv6')
		tf.histogram_summary('layer_6'  + '/biases', b_conv6)
	with tf.name_scope('h_conv6'):
		h_conv6 = tf.nn.relu(conv2d(h_conv5, W_conv6) + b_conv6)
	tf.histogram_summary('layer_6' + '/outputs', h_conv6)




with tf.name_scope('h_conv4_flat'):
	h_conv4_flat = tf.reshape(h_conv6, [-1, 15*15])



with tf.name_scope('prediction_softmax'):
	prediction = tf.nn.softmax(h_conv4_flat)

with tf.name_scope('cross_entropy'):
	cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))
	tf.scalar_summary('cross_entropy', cross_entropy)
with tf.name_scope('train'):
	train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

with tf.name_scope('prediction'):
	pre_loc = tf.argmax(prediction,1)

sess = tf.Session()


Data = DataCenter.MongoDB()

sess.run(tf.initialize_all_variables())

merged = tf.merge_all_summaries()
Data = DataCenter.MongoDB()
writer = tf.train.SummaryWriter("logs/", sess.graph)
for i in range(train_iters):
	print i
	x = Data.SGFReturnSet()
	y = Data.SGFReturnAnw()
	cut_color = Data.ReturnColor()
	x_8_24_stack = game.ReturnAllLayer (x, cut_color)
	y_8_stack = game.Return_Eight_Layer (y )
	sess.run(train_step, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
	result = sess.run(merged,feed_dict={xs: x_8_24_stack, ys: y_8_stack})
	writer.add_summary(result, i)



sess.close()





