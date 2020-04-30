import datetime

def date():
	# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
	currentDate = datetime.date.today().strftime("%d/%m/%Y")
	print(currentDate)
 
    # 创建日期对象
	makeAdate = datetime.date(2020,1,24)
	print(makeAdate.strftime("%d/%m/%Y"))

    # 日期算术运算
	newDate = makeAdate + datetime.timedelta(days=1)
	print(newDate.strftime("%d/%m/%Y"))
 
    # 日期替换
	newYear = makeAdate.replace(year=1991,month=1,day=24)
	print(newYear.strftime("%d/%m/%Y"))



if __name__ == "__main__":
	date()