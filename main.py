from MongoDB import DataCenter
import tensorflow as tf
import numpy as np

# Parameters
learning_rate = 0.001
training_iters = 200000
test_iters = 10000
display_step = 10000

# Network Parameters
n_input =225 # alphaGo data input (img shape: 19*19)
n_classes = 225 # AlphaGo total classes (19x19=361 digits)
dropout = 0.618 # Dropout, probability to keep units

# tf Graph input
x = tf.placeholder(tf.float32, [1, n_input])
y = tf.placeholder(tf.float32, [1, n_classes])
keep_prob = tf.placeholder(tf.float32) # dropout (keep probability)

# Create custom model
def conv2d(name, l_input, w, b):
    return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(l_input, w, strides=[1, 1, 1, 1], padding='SAME'),b), name=name)

def max_pool(name, l_input, k):
    return tf.nn.max_pool(l_input, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME', name=name)

def norm(name, l_input, lsize=4):
    return tf.nn.lrn(l_input, lsize, bias=1.0, alpha=0.001 / 9.0, beta=0.75, name=name)

def alphago(_X, _weights, _biases, _dropout):
    # Reshape input picture
    _X = tf.reshape(_X, shape=[-1, 15, 15, 1])

    # Convolution Layer
    conv1 = conv2d('conv1', _X, _weights['wc1'], _biases['bc1'])
    print conv1
    # Max Pooling (down-sampling)
    pool1 = max_pool('pool1', conv1, k=2)
    print pool1
    # Apply Normalization
    norm1 = norm('norm1', pool1, lsize=4)
    print norm1
    # Apply Dropout
    norm1 = tf.nn.dropout(norm1, _dropout)
    #conv1 image show
    tf.image_summary("conv1", conv1)
    
    # Convolution Layer
    
    conv2 = conv2d('conv2', norm1, _weights['wc2'], _biases['bc2'])
    print conv2
    # Max Pooling (down-sampling)
    pool2 = max_pool('pool2', conv2, k=2)
    print pool2
    # Apply Normalization
    norm2 = norm('norm2', pool2, lsize=4)
    print norm2
    # Apply Dropout
    norm2 = tf.nn.dropout(norm2, _dropout)

    # Convolution Layer
    conv3 = conv2d('conv3', norm2, _weights['wc3'], _biases['bc3'])
    print conv3
    # Max Pooling (down-sampling)
    pool3 = max_pool('pool3', conv3, k=2)
    print pool3
    # Apply Normalization
    norm3 = norm('norm3', pool3, lsize=4)
    
    # Apply Dropout
    norm3 = tf.nn.dropout(norm3, _dropout)
   
    # Fully connected layer
    print norm3
    print _weights['wd1'].get_shape().as_list()[0]
    dense1 = tf.reshape(norm3, [-1, _weights['wd1'].get_shape().as_list()[0]]) # Reshape conv3 output to fit dense layer input
    dense1 = tf.nn.relu(tf.matmul(dense1, _weights['wd1']) + _biases['bd1'], name='fc1') # Relu activation

    dense2 = tf.nn.relu(tf.matmul(dense1, _weights['wd2']) + _biases['bd2'], name='fc2') # Relu activation
    print dense2
    # Output, class prediction
    out = tf.matmul(dense2, _weights['out']) + _biases['out']
    return out

# Store layers weight & bias
weights = {
    'wc1': tf.Variable(tf.random_normal([3, 3, 1, 64])),
    'wc2': tf.Variable(tf.random_normal([3, 3, 64, 128])),
    'wc3': tf.Variable(tf.random_normal([3, 3, 128, 256])),
    'wd1': tf.Variable(tf.random_normal([2*2*256, 1024])), 
    'wd2': tf.Variable(tf.random_normal([1024, 1024])),
    'out': tf.Variable(tf.random_normal([1024, n_classes]))
}
biases = {
    'bc1': tf.Variable(tf.random_normal([64])),
    'bc2': tf.Variable(tf.random_normal([128])),
    'bc3': tf.Variable(tf.random_normal([256])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'bd2': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = alphago(x, weights, biases, keep_prob)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Evaluate model
y_estimate = tf.argmax(pred,1)

# Initializing the variables
init = tf.initialize_all_variables()
# 
tf.scalar_summary("loss", cost)
# Merge all summaries to a single operator
merged_summary_op = tf.merge_all_summaries()
# Launch the graph
Data = DataCenter.MongoDB()

with tf.Session() as sess:
    sess.run(init)
    summary_writer = tf.train.SummaryWriter('/tmp/logs', graph_def=sess.graph_def)
    step = 1
    # Keep training until reach max iterations
    for step in range(training_iters):
    	set_x = Data.SGFReturnSet()
    	out_y = Data.SGFReturnAnw()
        

    	sess.run(optimizer, feed_dict={x: np.reshape(set_x,[1,225]), y: np.reshape(out_y,[1,225]), keep_prob: 1.})
    	if step %100 ==0:
    		print step
    	

    count = 0
    for i in range(test_iters):
    	set_x = Data.SGFReturnSet()
    	out_y = Data.SGFReturnAnw()
    	acc = sess.run(y_estimate, feed_dict={x: np.reshape(set_x,[1,225]), y: np.reshape(out_y,[1,225]), keep_prob: 1.})
    	num_list = acc.tolist()
    	num = num_list[0]
    	if np.argmax(out_y) == num:
    		count = count + 1

    print count
    print "Optimization Finished!"
    # Calculate accuracy for 256 mnist test images
