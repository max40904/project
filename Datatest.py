from MongoDB import DataCenter
training_iters = 500000
Data = DataCenter.MongoDB()

for i in range(training_iters):
	print i
	set_x = Data.SGFReturnSet()
	out_y = Data.SGFReturnAnw()