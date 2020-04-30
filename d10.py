#暂停一秒输出，并格式化当前时间。
import time


def formatTime():
	print(time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime(time.time())))


if __name__ == "__main__":
	time.sleep(1)
	formatTime()