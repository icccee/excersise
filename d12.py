

#题目：判断101-200之间有多少个素数，并输出所有素数。

import math


# to determine if a num is a prime or not
# divide the number from 0 to its sqrt

def isPrime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	
	return True

def primeTotal(From=0,To=0):
	totalPrime = 0

	if From > To:
		print("invalid range")
	for i in range(From,To+1):
		if isPrime(i):
			totalPrime +=1
			print(i)
	
	print("Total Prime number between {0} to {1} is {2}".format(From,To,totalPrime))


primeTotal(101,200)