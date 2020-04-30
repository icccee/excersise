# 输出 9*9 乘法口诀表。


def printMultiPrcpl():
	for i in range(1,10):
		print()
		for j in range(1,i+1):
			print("{0} x {1} = {2}".format(i,j,i*j),end='  ')

	print()




if __name__ == "__main__":
	printMultiPrcpl()