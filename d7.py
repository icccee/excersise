#将一个列表的数据复制到另一个列表中


# 1

def copyList_1(lst):
	return lst[:]

# 2

def copyList_2(lst):
	return lst.copy()



def main():
	lst = [1,2,3]
	# copy a list 
	lstA = copyList_1(lst)
	lstB = copyList_2(lst)

	print(lstA,"\n",lstB)
	# make changes

	lst.append(4)

	print(lst,"\n",lstA,"\n",lstB)

if __name__ == "__main__":
	main()



