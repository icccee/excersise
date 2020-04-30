# 题目：暂停一秒输出。
# lets make a count down timer
# user input the sec




import time

#"""
def countDown(sec = 0):
	try:
		while sec > 0:
			print(sec,'\r',end='')
			sec -= 1
			time.sleep(1)
	except:
		print("Nothing entered!")



if __name__ == "__main__":
	#count down 10sec
	countDown(10)
	#catch error
	countDown(0)
	
"""

def backline():        
    print('\r', end='')                     # use '\r' to go back


for i in range(101):                        # for 0 to 100
    s = str(i) + '%'                        # string for output
    print(s,end='')                        # just print and flush
    backline()                              # back to the beginning of line    
    time.sleep(0.2)       

"""