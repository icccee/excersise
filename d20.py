#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？



"""
10 -> 5 
5 -> 2.5
2.5 ->1.25

....
"""



# float
def jumpBack(meter,n):
	total = meter
	tenthHeight = 0

	while n > 1:
		meter /= 2
		total += meter * 2
		n -= 1
		if n == 1:
			tenthHeight = meter/2
	
	return total, tenthHeight

print(jumpBack(100.0,10))

