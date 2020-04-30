# 输入三个整数x,y,z，请把这三个数由小到大输出。



#using sort() func
def enterNsorting():
	l = []
	for _ in range(3):
		l.append(int(input("Enter a number: ")))
	l.sort()
	print(l)



# hardcode 

def insertionSort(lst):
	pass
def enterNsorting_hardcode():
	l = []
	for _ in range(3):
		n = int(input("Enter a number: "))
		
		l.append(n)

	print(l)



if __name__ == "__main__":
	#enterNsorting()
	enterNsorting_hardcode()


