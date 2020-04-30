

#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。



# range(100 - 1000)



def isDesinatedNumber(a):

	i = a // 100
	j = a // 10 % 10
	k = a % 10

	if a == i**3 + j**3 + k**3:
		return True
	
	return False



def main():
	result = []
	for i in range(100,1000):
		if isDesinatedNumber(i):
			result.append(i)
	
	print(result)



if __name__ == "__main__":
	main()