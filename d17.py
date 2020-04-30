#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。




def countCharacters(string):
	ch = 0
	num = 0
	space = 0
	others = 0

	for i in string:
		if i.isalpha():
			ch += 1
		elif i.isdigit():
			num += 1
		elif i.isspace():
			space += 1
		else:
			others += 1
	
	print("{0} has {1} characters,{2} numbers, {3} spaces and {4} symbols.".format(string,ch,num,space,others))






countCharacters("123runoobc  kdf235*(dfl")