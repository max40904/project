import tensorflow as tf



class ValueNetwork:
	

	def __init__(self, learning, input_stack, k_filter,seed):
		self.learning_rate = learning
		self.input_stack = input_stack
		self.k_filter = k_filter
		self.seed = seed
		with tf.name_scope('input'):
			self.xs = tf.placeholder(tf.float32, [None, 15,15,input_stack],name = 'x_input')
			self.ys = tf.placeholder(tf.float32, [None, 1], name = 'y_input')


		
		with tf.name_scope('layer_1'):
			with tf.name_scope('weight'):
				self.W_conv1 = self.__weight_variable([5, 5, input_stack, k_filter],'W_conv1')
				tf.histogram_summary('layer_1' + '/weights', self.W_conv1)
			with tf.name_scope('biases'):
				self.b_conv1 = self.__bias_variable([k_filter],'b_conv1')
				tf.histogram_summary('layer_1'  + '/biases', self.b_conv1)
			with tf.name_scope('h_conv1'):
				self.h_conv1 = tf.nn.relu(self.__conv2d(self.xs, self.W_conv1) + self.b_conv1)
			tf.histogram_summary('layer_1' + '/outputs', self.h_conv1)

		with tf.name_scope('layer_2'):
			with tf.name_scope('weighs'):
				self.W_conv2 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv2')
				tf.histogram_summary('layer_2' + '/weights', self.W_conv2)
			with tf.name_scope('biases'):
				self.b_conv2 = self.__bias_variable([k_filter],'b_conv2')
				tf.histogram_summary('layer_2'  + '/biases', self.b_conv2)
			with tf.name_scope('h_conv2'):
				self.h_conv2 = tf.nn.relu(self.__conv2d(self.h_conv1, self.W_conv2) + self.b_conv2)
			tf.histogram_summary('layer_2' + '/outputs', self.h_conv2)

		with tf.name_scope('layer_3'):
			with tf.name_scope('weighs'):
				self.W_conv3 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv3')
				tf.histogram_summary('layer_3' + '/weights', self.W_conv3)
			with tf.name_scope('biases'):
				self.b_conv3 = self.__bias_variable([k_filter],'b_conv3')
				tf.histogram_summary('layer_3'  + '/biases', self.b_conv3)
			with tf.name_scope('h_conv3'):
				self.h_conv3 = tf.nn.relu(self.__conv2d(self.h_conv2, self.W_conv3) + self.b_conv3)
			tf.histogram_summary('layer_3' + '/outputs', self.h_conv3)


		with tf.name_scope('layer_4'):
			with tf.name_scope('weighs'):
				self.W_conv4 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv4')
				tf.histogram_summary('layer_4' + '/weights', self.W_conv4)
			with tf.name_scope('biases'):
				self.b_conv4 = self.__bias_variable([k_filter],'b_conv4')
				tf.histogram_summary('layer_4'  + '/biases', self.b_conv4)
			with tf.name_scope('h_conv4'):
				self.h_conv4 = tf.nn.relu(self.__conv2d(self.h_conv3, self.W_conv4) + self.b_conv4)
			tf.histogram_summary('layer_4' + '/outputs', self.h_conv4)

		with tf.name_scope('layer_5'):
			with tf.name_scope('weighs'):
				self.W_conv5 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv5')
				tf.histogram_summary('layer_5' + '/weights', self.W_conv5)
			with tf.name_scope('biases'):
				self.b_conv5 = self.__bias_variable([k_filter],'b_conv5')
				tf.histogram_summary('layer_5'  + '/biases', self.b_conv5)
			with tf.name_scope('h_conv5'):
				self.h_conv5 = tf.nn.relu(self.__conv2d(self.h_conv4, self.W_conv5) + self.b_conv5)
			tf.histogram_summary('layer_5' + '/outputs', self.h_conv5)

		with tf.name_scope('layer_6'):
			with tf.name_scope('weighs'):
				self.W_conv6 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv6')
				tf.histogram_summary('layer_6' + '/weights', self.W_conv6)
			with tf.name_scope('biases'):
				self.b_conv6 = self.__bias_variable([k_filter],'b_conv6')
				tf.histogram_summary('layer_6'  + '/biases', self.b_conv6)
			with tf.name_scope('h_conv6'):
				self.h_conv6 = tf.nn.relu(self.__conv2d(self.h_conv5, self.W_conv6) + self.b_conv6)
			tf.histogram_summary('layer_6' + '/outputs', self.h_conv6)

		with tf.name_scope('layer_7'):
			with tf.name_scope('weighs'):
				self.W_conv7 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv7')
				tf.histogram_summary('layer_7' + '/weights', self.W_conv7)
			with tf.name_scope('biases'):
				self.b_conv7 = self.__bias_variable([k_filter],'b_conv7')
				tf.histogram_summary('layer_7'  + '/biases', self.b_conv7)
			with tf.name_scope('h_conv7'):
				self.h_conv7 = tf.nn.relu(self.__conv2d(self.h_conv6, self.W_conv7) + self.b_conv7)
			tf.histogram_summary('layer_7' + '/outputs', self.h_conv7)

		with tf.name_scope('layer_8'):
			with tf.name_scope('weighs'):
				self.W_conv8 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv8')
				tf.histogram_summary('layer_8' + '/weights', self.W_conv8)
			with tf.name_scope('biases'):
				self.b_conv8 = self.__bias_variable([k_filter],'b_conv8')
				tf.histogram_summary('layer_8'  + '/biases', self.b_conv8)
			with tf.name_scope('h_conv8'):
				self.h_conv8 = tf.nn.relu(self.__conv2d(self.h_conv7, self.W_conv8) + self.b_conv8)
			tf.histogram_summary('layer_8' + '/outputs', self.h_conv8)

		with tf.name_scope('layer_9'):
			with tf.name_scope('weighs'):
				self.W_conv9 = self.__weight_variable([3, 3, k_filter, k_filter],'W_conv9')
				tf.histogram_summary('layer_9' + '/weights', self.W_conv9)
			with tf.name_scope('biases'):
				self.b_conv9 = self.__bias_variable([k_filter],'b_conv9')
				tf.histogram_summary('layer_9'  + '/biases', self.b_conv9)
			with tf.name_scope('h_conv9'):
				self.h_conv9 = tf.nn.relu(self.__conv2d(self.h_conv8, self.W_conv9) + self.b_conv9)
			tf.histogram_summary('layer_9' + '/outputs', self.h_conv9)

		

		

		


		
		with tf.name_scope('layer_13'):
			with tf.name_scope('weighs'):
				self.W_conv13 = self.__weight_variable([1, 1, k_filter, 1],'W_conv13')
				tf.histogram_summary('layer_13' + '/weights', self.W_conv13)
			with tf.name_scope('biases'):
				self.b_conv13 = self.__bias_variable([1],'b_conv13')
				tf.histogram_summary('layer_13'  + '/biases', self.b_conv13)
			with tf.name_scope('h_conv13'):
				self.h_conv13 = tf.nn.relu(self.__conv2d(self.h_conv9, self.W_conv13) + self.b_conv13)
			tf.histogram_summary('layer_13' + '/outputs', self.h_conv13)


		with tf.name_scope('h_conv_flat'):
			self.h_conv_flat = tf.reshape(self.h_conv13, [-1, 15*15*1])


		with tf.name_scope('layer_14'):
			with tf.name_scope('weighs'):
				self.W_fc1 = self.__weight_variable([15*15*1,128],'W_fc1')
				tf.histogram_summary('layer_14' + '/weights', self.W_fc1)
			with tf.name_scope('biases'):
				self.b_fc1 = self.__bias_variable([128],'b_fc1')
				tf.histogram_summary('layer_14'  + '/biases', self.b_fc1)
			with tf.name_scope('h_fc1'):
				self.h_fc1 = tf.nn.relu(tf.matmul(self.h_conv_flat, self.W_fc1) + self.b_fc1)
			tf.histogram_summary('layer_14' + '/outputs', self.h_fc1)

		with tf.name_scope('layer_15'):
			with tf.name_scope('weighs'):
				self.W_fc2 = self.__weight_variable([128,1],'W_fc2')
				tf.histogram_summary('layer_15' + '/weights', self.W_fc2)
			with tf.name_scope('biases'):
				self.b_fc2 = self.__bias_variable([1],'b_fc2')
				tf.histogram_summary('layer_15'  + '/biases', self.b_fc2)
			with tf.name_scope('h_fc1'):
				self.h_fc2 = tf.nn.tanh(tf.matmul(self.h_fc1, self.W_fc2) + self.b_fc2)
			tf.histogram_summary('layer_15' + '/outputs', self.h_fc2)
		

		with tf.name_scope('prediction'):
			self.predic = self.h_fc2
		with tf.name_scope('cross_entropy'):
			self.cost = (self.ys - self.predic)*self.predic
			self.cross_entropy = -tf.reduce_mean(self.cost) 
			tf.scalar_summary('cross_entropy', self.cross_entropy)


		with tf.name_scope('train'):
			self.train_step = tf.train.GradientDescentOptimizer(learning).minimize(self.cross_entropy)
		with tf.name_scope('prediction'):
			self.pre_loc = tf.argmax(self.predic,1)
		self.sess = tf.Session()
		self.saver = tf.train.Saver()
		self.merged = tf.merge_all_summaries()
		self.writer = tf.train.SummaryWriter("logs_Value/", self.sess.graph)
		



	def initialize(self):
		self.sess.run(tf.initialize_all_variables())

	def restore(self, loc_str):
		self.saver.restore(self.sess, loc_str)

	def savedata(self, loc_str):
		save_path = self.saver.save(self.sess, loc_str)
		print("Save to path: ", save_path)


	def train(self, input, output):
		self.sess.run(self.train_step, feed_dict = {self.xs: input,self.ys :output})
	
	
	def Return_cross_entropy(self, input, output):
		cross =  self.sess.run(self.cost, feed_dict = {self.xs: input,self.ys :output})
		return cross
	def Return_prediction_prob_empty(self,input,output):
		pre =  self.sess.run(self.predic , feed_dict = {self.xs: input,self.ys :output})
		return pre[0][0]
	def Return_prediction_prob_black(self,input,output):
		pre =  self.sess.run(self.predic , feed_dict = {self.xs: input,self.ys :output})
		return pre[0][1]
	def Return_prediction_prob_white(self,input,output):
		pre =  self.sess.run(self.predic , feed_dict = {self.xs: input,self.ys :output})
		return pre[0][2]

	def Return_prediction(self,input,output):
		pre =  self.sess.run(self.pre_loc, feed_dict = {self.xs: input,self.ys :output})
		return pre[0]
	def draw(self, input, output, i):
		result = self.sess.run(self.merged,feed_dict={self.xs:input, self.ys : output})
		self.writer.add_summary(result,i)


	def __weight_variable(self,shape,names):
		initial = tf.random_uniform(shape, minval=-0.1, maxval=0.1, dtype=tf.float32, seed=self.seed, name=names)
		return tf.Variable(initial)

	def __bias_variable(self,shape, names):
		initial = tf.constant(0.1, shape = shape,  name = names)
		return tf.Variable(initial)

	def __conv2d(self, x ,W):
		return tf.nn.conv2d(x, W, strides = [1, 1, 1, 1], padding = 'SAME')

	# def __del__(self):
	# 	self.sess.close()



