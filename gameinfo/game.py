
from __future__ import print_function

def gameshow( set):
	for i in range(225):
		if i %15 ==0:
			print ("")
		if set[i] == 1:
			print("@ ", end="")

			
		elif set[i] ==0.5:
			print("# ", end="")

			
		else :
			print('. ', end="")

	print ("\n")

