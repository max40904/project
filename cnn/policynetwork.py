import tensorflow as tf
import numpy as np



class policynetwork:
	

	def __init__(self, learning, input_stack, k_filter, train_iter):
		self.learning_rate = learning
		self.input_stack = input_stack
		self.k_filter = k_filter
		self.train_iter = train_iter


		self.xs = tf.placeholder(tf.float32, [None, 15,15,input_stack])
		self.ys = tf.placeholder(tf.float32, [None, 225])


		self.W_conv1 = __weight_variable([5, 5, input_stack, k_filter])
		self.b_conv1 = __bias_variable([k_filter])
		self.h_conv1 = tf.nn.relu(conv2d(xs, W_conv1) + b_conv1)


		self.W_conv2 = __weight_variable([3, 3, k_filter, k_filter])
		self.b_conv2 = __bias_variable([k_filter])
		self.h_conv2 = tf.nn.relu(conv2d(h_conv1, W_conv2) + b_conv2)


		self.W_conv3 = __weight_variable([3, 3, k_filter, k_filter])
		self.b_conv3 = __bias_variable([k_filter])
		self.h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3) + b_conv3)


		self.W_conv4 = __weight_variable([3, 3, k_filter, k_filter])
		self.b_conv4 = __bias_variable([k_filter])
		self.h_conv4 = tf.nn.relu(conv2d(h_conv3, W_conv4) + b_conv4) 

		self.W_conv5 = __weight_variable([3, 3, k_filter, k_filter])
		self.b_conv5 = __bias_variable([k_filter])
		self.h_conv5 = tf.nn.relu(conv2d(h_conv4, W_conv5) + b_conv5)

		self.W_conv6 = __weight_variable([1, 1, k_filter, 1])
		self.b_conv6 = __bias_variable([1])
		self.h_conv6 = tf.nn.relu(conv2d(h_conv5, W_conv6) + b_conv6)

		self.h_conv4_flat = tf.reshape(h_conv6, [-1, 15*15])
		self.prediction = tf.nn.softmax(h_conv4_flat)
		self.cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))   
		self.train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
		self.pre_loc = tf.argmax(prediction,1)
		self.sess = tf.Session()
		self.sess.run(tf.initialize_all_variables())

	def __weight_variable(self,shape):
		initial = tf.truncated_normal(shape,stddev =  0.1)
		return tf.Variable(initial)

	def __bias_variable(self,shape):
		initial = tf.constant(0.1, shape = shape)
		return tf.Variable(initial)

	def conv2d(self, x ,W):
		return tf.nn.conv2d(x, W, stride = [1, 1, 1, 1], padding = 'SAME')


	def train(self, input, output):
		self.sess.run(self.train_step, feed_dict = {xs: input,ys :output})


	def cross_entropy(self, input, output):
		cross =  sess.run(cross_entropy, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
		return cross[0]

	def prediction(self,input,output):
		pre = self.sess.run(self.pre_loc, feed_dict = {xs: x_8_24_stack,ys :y_8_stack})
		return pre[0]


