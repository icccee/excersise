

#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？



"""
sudo code

m1 - 1 pair
m2 - 1 
m3 - 2
m4 - 3
m5 - 5
......


mn - (m-1) + (m-2)

finoccino

"""


def fib(n):
	if n < 3:
		return 1
	return fib(n-1) + fib(n-2)


def month():
	i = 1
	while i < 13:
		print(fib(i))
		i += 1

if __name__ == "__main__":
	month()