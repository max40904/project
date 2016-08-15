import tensorflow as tf
from MongoDB import DataCenter 
from gameinfo import game
import numpy as np

learning_rate = 0.0003
input_stack = 24

k_filter = 24 * 4
training_iters = 1000


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(100., shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    # stride [1, x_movement, y_movement, 1]
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

# define placeholder for inputs to network
input = tf.placeholder(tf.float32, [None, 15,15,input_stack]) # 28x28
output = tf.placeholder(tf.float32, [None, 225])


w_conv1 = weight_variable([5,5,input_stack,k_filter])
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
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
init = tf.initialize_all_variables()

Data = DataCenter.MongoDB()

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "./Neural_network_save/save_net.ckpt")
    for i in range(10):
        set_x = Data.SGFReturnSet()
        out_y = Data.SGFReturnAnw()
        cur_color = Data.ReturnColor()
        all_layer_1 = game.ReturnAllInfo(set_x,cur_color)
        pre = sess.run(y_estimate, feed_dict={input: np.reshape(all_layer_1,[1,15,15,24]), output: np.reshape(out_y,[1,225])})
        pre_num = int(pre[0])
        game.show_game(np.reshape(out_y,[225,1]))
        game.show_game_pos(pre_num)