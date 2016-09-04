from MongoDB import DataCenter
from gameinfo import game
Data = DataCenter.MongoDB()
Data2 = DataCenter.MongoDB()
count = Data.allset
training_iters =  0
for i in range(1,count):
	temp  =  Data.Find(i)
	training_iters +=len(temp["Set"])
	print training_iters
	

for i in range(training_iters):
	set_x = Data.SGFReturnSet()
	out_y = Data.SGFReturnAnw()
	color = Data.ReturnColor()
	test = game.ReturnAllLayer(set_x, color )
	
	set_x_before =   Data2.SGFReturnSet()
	out_y =   Data2.SGFReturnAnw()
	before_eight = Data2.SGFReturnBefore()
	color = Data2.ReturnColor()
	# test2 = game.ReturnAllLayer_before(set_x_before, color,before_eight )
	print i


print "All Clear"