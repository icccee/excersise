#斐波那契数列。

class Fibonacci():

	def __init__(self,total):
		self.total = total
		self.fib = [0,1]

	def theNthFib(self):
		for i in range(self.total+1):
			if i < 2:
				pass
			else:
				fn = self.fib[i-2]+self.fib[i-1]
				self.fib.append(fn)
		return self.fib[self.total]

	def firstNfib(self):
		return(self.fib)



fib = Fibonacci(10)
print(fib.theNthFib())
print(fib.firstNfib())