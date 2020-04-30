#：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。




def Grade(score=0):
	if score >= 90:
		return "A"
	elif score > 60:
		return 'B'
	else:
		return 'C'


def main():

	print(Grade(100))
	print(Grade(89))
	print(Grade(60))
	print(Grade(70))
	


if __name__ == "__main__":
	main()