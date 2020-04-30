"输入某年某月某日，判断这一天是这一年的第几天？"

def isLeapYear(year):
	"""
	The year can be evenly divided by 4;
	If the year can be evenly divided by 100, it is NOT a leap year, unless;
	The year is also evenly divisible by 400. Then it is a leap year.
	"""
	if year % 100 == 0:
		if year % 400 == 0:
			return True
	elif year % 4 == 0:
		return True
	else:
		return False

def theNthDayofYear():

	daysInMonth = [0,31,28,31,30,31,31,30,31,30,31,30,31]

	nthDay = 0
	day = int(input("Enter the day: "))	
	month = int(input("Enter the month: "))
	year = int(input("Enter the year: "))
	try:
		
		nthDay += sum(daysInMonth[:month])

		if isLeapYear(year):
			nthDay += 1
		
		nthDay += day
		print("the {0}/{1}/{2} is {3}th day of the year {2}".format(month,day,year,nthDay))

	except SystemError:
		print("Wrong input")
	


if __name__ == "__main__":
	theNthDayofYear()
	