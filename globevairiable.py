import threading
import time

#定义全局变量
g_num = 0

def test1():
	"""函数test1对全局变量进行更改"""
	global g_num
	for i in range(1,10):
		g_num += 1

	print("--- test1 线程 g_num = %d--- " % g_num)

def test2():
	"""函数test2 打印全局变量"""
	print("--- test2 线程 g_num = %d--- " % g_num)

def main():
	t1 = threading.Thread(target=test1)
	t2 = threading.Thread(target=test2)

	# 启动线程
	t1.start()
	# 增加睡眠是为了保证优先执行函数test1
	time.sleep(1)
	t2.start()

	print("--- 主线程 g_num = %d--- " % g_num)

if __name__ == '__main__':
	main()