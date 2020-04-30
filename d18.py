



def sumThenumber(num,repeat):
	Sum = 0
	cons = num
	while repeat > 0:
		print(num)
		Sum += num
		num = num * 10 + cons
		repeat -= 1
	return Sum

print(sumThenumber(4,4))