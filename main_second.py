import tensorflow as tf
from MongoDB import DataCenter
from gameinfo import game
import numpy as np

learning_rate = 0.003
input_stack = 24
k_filter = input_stack * 2
train_iters = 400000



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


xs = tf.placeholder(tf.float32, [None, 15,15,input_stack]) # 28x28
ys = tf.placeholder(tf.float32, [None, 225])



W_conv1 = weight_variable([5, 5, input_stack, k_filter])
b_conv1 = bias_variable([k_filter])

h_conv1 = tf.nn.relu(conv2d(xs, W_conv1) + b_conv1) # 15*15*24 ->15*15*96

print h_conv1

W_conv2 = weight_variable([3, 3, k_filter, k_filter])
b_conv2 = bias_variable([k_filter])

h_conv2 = tf.nn.relu(conv2d(h_conv1, W_conv2) + b_conv2) 
# 15 * 15 * 96 -> 15 * 15 *96
print h_conv2


W_conv3 = weight_variable([3, 3, k_filter, k_filter])
b_conv3 = bias_variable([k_filter])
h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3) + b_conv3) 
# 15 * 15 * 96 -> 15 * 15 *96
print h_conv3
W_conv4 = weight_variable([3, 3, k_filter, k_filter])
b_conv4 = bias_variable([k_filter])
h_conv4 = tf.nn.relu(conv2d(h_conv3, W_conv4) + b_conv4) 
# 15 * 15 * 96 -> 15 * 15 *96
print h_conv4


W_conv5 = weight_variable([3, 3, k_filter, k_filter])
b_conv5 = bias_variable([k_filter])
h_conv5 = tf.nn.relu(conv2d(h_conv4, W_conv5) + b_conv5) 
# 15 * 15 * 96 -> 15 * 15 *96
print h_conv4

W_conv6 = weight_variable([1, 1, k_filter, 1])
b_conv6 = bias_variable([1])
h_conv6 = tf.nn.relu(conv2d(h_conv5, W_conv6) + b_conv6) # 15 * 15 * 96 -> 15 * 15 *96
print h_conv6



h_conv4_flat = tf.reshape(h_conv6, [-1, 15*15])
print h_conv4_flat

prediction = tf.nn.softmax(h_conv4_flat)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))   
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

pre_loc = tf.argmax(prediction,1)

sess = tf.Session()

sess.run(tf.initialize_all_variables())
print sess.run(W_conv1)[0][0]

Data = DataCenter.MongoDB()
saver = tf.train.Saver()
for i in range(train_iters):
	print i
	x = Data.SGFReturnSet()
	y = Data.SGFReturnAnw()
	cut_color = Data.ReturnColor()
	x_8_24_stack = game.ReturnAllLayer (x, cut_color)
	y_8_stack = game.Return_Eight_Layer (y )
	sess.run(train_step, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
	bbb =  sess.run(cross_entropy, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
	print bbb
	if i %10000 ==0:
		save_path = saver.save(sess, "./Neural_network_save/save_net"+str(i)+".ckpt")
		print("Save to path: ", save_path)
	
Data2 = DataCenter.MongoDB()




for i in range(train_iters):
	print i
	x = Data2.SGFReturnSet()
	y = Data2.SGFReturnAnw()
	cut_color = Data2.ReturnColor()
	x_8_24_stack = np.reshape(game.ReturnAllInfo (x, cut_color),[1,15,15,24])
	y_8_stack = np.reshape(y,[1,225]) 
	y_estimate =  sess.run(pre_loc, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
	num= y_estimate[0]
	game.show_game(np.reshape(x,[225,1]))
	game.show_game(np.reshape(y,[225,1]))
	game.show_game_set(num)
	a = raw_input()