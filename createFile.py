


# enter the number of same type files you want to create
# enter the file format
def createFile(Name,n,filetype):
	for i in range(1,n+1):
		fileName = Name+str(i)+ '.'+filetype
		with open(fileName,'x') as f:
			f.close()


if __name__ == "__main__":
	createFile("hello",2,'txt')