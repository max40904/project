from MongoDB import DataCenter
import tensorflow as tf
import numpy as np
Data = DataCenter.MongoDB()
x_input = tf.placeholder(tf.float32,[None,225])#15*15 input

W = tf.Variable(tf.zeros([225,225]))
b =tf.Variable(tf.zeros([225]))
y = tf.nn.softmax(tf.matmul(x_input, W) + b)
y_input = tf.placeholder(tf.float32,[None,225]) #15*15 output
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_input * tf.log(y), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess = tf.Session()
init = tf.initialize_all_variables()

sess.run(init)
for i in range(100):
	set_x = Data.ReturnSet()
	out_y = Data.ReturnAnw()
	sess.run(train_step, feed_dict={x_input: [np.reshape(set_x,225)], y_input: [np.reshape(out_y,225)]})






