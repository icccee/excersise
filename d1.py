"""
题目：有四个数字：1、2、3、4，
能组成多少个互不相同且无重复数字的三位数？各是多少？

"""
def combo(a,b,c,d):
	result=[]
	lst = [a,b,c,d]
	for i in lst:
		for j in lst:
			for k in lst:
				if i != j and i != k and j != k:
					result.append([i,j,k])
	return result

result = combo(1,2,3,4)

answer = [
	[1,2,3],
	[1,2,4],
	[1,3,2],
	[1,3,4],
	[1,4,2],
	[1,4,3],
	[2,1,3],
	[2,1,4],
	[2,3,1],
	[2,3,4],
	[2,4,1],
	[2,4,3],
	[3,1,2],
	[3,1,4],
	[3,2,1],
	[3,2,4],
	[3,4,1],
	[3,4,2],
	[4,1,2],
	[4,1,3],
	[4,2,1],
	[4,2,3],
	[4,3,1],
	[4,3,2],
]

if result == answer:
	print("DONE")
else:
	print('sth wrong')