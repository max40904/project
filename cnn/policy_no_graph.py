import tensorflow as tf



class PolicyNetwork:
	

	def __init__(self, learning, input_stack, k_filter):
		self.learning_rate = learning
		self.input_stack = input_stack
		self.k_filter = k_filter
	


		self.xs = tf.placeholder(tf.float32, [None, 15,15,input_stack])
		self.ys = tf.placeholder(tf.float32, [None, 225])


		self.W_conv1 = self.__weight_variable([5, 5, input_stack, k_filter])
		self.b_conv1 = self.__bias_variable([k_filter])
		self.h_conv1 = tf.nn.relu(self.__conv2d(self.xs, self.W_conv1) + self.b_conv1)


		self.W_conv2 = self.__weight_variable([3, 3, k_filter, k_filter])
		self.b_conv2 = self.__bias_variable([k_filter])
		self.h_conv2 = tf.nn.relu(self.__conv2d(self.h_conv1, self.W_conv2) + self.b_conv2)


		self.W_conv3 = self.__weight_variable([3, 3, k_filter, k_filter])
		self.b_conv3 = self.__bias_variable([k_filter])
		self.h_conv3 = tf.nn.relu(self.__conv2d(self.h_conv2, self.W_conv3) + self.b_conv3)


		self.W_conv4 = self.__weight_variable([3, 3, k_filter, k_filter])
		self.b_conv4 = self.__bias_variable([k_filter])
		self.h_conv4 = tf.nn.relu(self.__conv2d(self.h_conv3, self.W_conv4) + self.b_conv4) 

		self.W_conv5 = self.__weight_variable([3, 3, k_filter, k_filter])
		self.b_conv5 = self.__bias_variable([k_filter])
		self.h_conv5 = tf.nn.relu(self.__conv2d(self.h_conv4, self.W_conv5) + self.b_conv5)

		self.W_conv6 = self.__weight_variable([1, 1, k_filter, 1])
		self.b_conv6 = self.__bias_variable([1])
		self.h_conv6 = tf.nn.relu(self.__conv2d(self.h_conv5, self.W_conv6) + self.b_conv6)

		self.h_conv4_flat = tf.reshape(self.h_conv6, [-1, 15*15])
		self.predic = tf.nn.softmax(self.h_conv4_flat)
		self.cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.ys * tf.log(self.predic),
                                              reduction_indices=[1]))   
		self.train_step = tf.train.GradientDescentOptimizer(learning).minimize(self.cross_entropy)
		self.pre_loc = tf.argmax(self.predic,1)
		self.sess = tf.Session()
		self.saver = tf.train.Saver()



	def initialize(self):
		self.sess.run(tf.initialize_all_variables())

	def restore(self, loc_str):
		self.saver.restore(self.sess, loc_str)

	def savedata(self, loc_str):
		save_path = self.saver.save(self.sess, loc_str)
		print("Save to path: ", save_path)


	def train(self, input, output):
		self.sess.run(self.train_step, feed_dict = {self.xs: input,self.ys :output})


	def cross_entropy(self, input, output):
		cross =  self.sess.run(cross_entropy, feed_dict = {self.xs: input,self.ys :output})
		return cross[0]

	def prediction(self,input,output):
		pre =  self.sess.run(self.pre_loc, feed_dict = {self.xs: input,self.ys :output})
		return pre[0] 

	def __weight_variable(self,shape):
		initial = tf.truncated_normal(shape,stddev =  0.1)
		return tf.Variable(initial)

	def __bias_variable(self,shape):
		initial = tf.constant(0.1, shape = shape)
		return tf.Variable(initial)

	def __conv2d(self, x ,W):
		return tf.nn.conv2d(x, W, strides = [1, 1, 1, 1], padding = 'SAME')

	def __del__(self):
		self.sess.close()



