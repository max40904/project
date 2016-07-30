file = open("list_sgf","r")
content = file.read()
content = content.split("\n")
for i in range(len(content)):
	f2 = open(str(i),"w")
	f2.write(content[i])
	f2.close()


file.close()