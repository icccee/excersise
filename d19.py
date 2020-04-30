#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。




# range < 1000
# n / 2



def findNumber(n):
	lst = []
	for i in range(1,int(n/2)+1):
		if n % i == 0:
			lst.append(i)

	if sum(lst) == n:
		print(lst)
		return True



for i in range(2,1001):
	if findNumber(i):
		print(i)

