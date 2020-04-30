#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math

def isPrime(n):

	for i in range(2,int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	
	return True



# tracking the number range from 2-sqrt(n)
# until n is a prime

def numberDivide(n):

	
	if isinstance(n, int) and n > 0:

		if isPrime(n):
			#print(n)
			return n
		for i in range(2,int(math.sqrt(n)+1)):
			if isPrime(i) and n % i == 0:
				#print(i)
				n //= i 
				return str(i)+ str(numberDivide(n))

def printFormat(n):
	try:
		if n > 0:
			s = numberDivide(n)
			print('{0} ='.format(n),' x '.join(s))
	except:
		print("doe")

if __name__ == "__main__":
	printFormat(10)
	printFormat(90)
	printFormat(100)
	printFormat(1000)
	printFormat(0)
	printFormat(-2)



			