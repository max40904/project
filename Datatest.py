from MongoDB import DataCenter
from gameinfo import game
Data = DataCenter.MongoDB("Gamedata")
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
	

	print i


print "All Clear"