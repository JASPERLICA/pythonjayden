import threading
import queue
import time
#创建一个队列，1代表maxSize
q=queue.Queue(1)  #创建一个先进先出的队列
#q=queue.LifoQueue  #创建一个后进先出的队列
#q=queue.PriorityQueue  #优先级的队列

#定义生产者线程
class Producer(threading.Thread):

    def run(self):
        global q
        count=0
        while True:
            time.sleep(5)
            print("生产线程开始生产数据")
            count+=1
            msg="产品{}".format(count)
            q.put(msg)        #默认阻塞
            print(msg)
#定义消费者线程
class Consumer(threading.Thread):

    def run(self):
        global q
        while True:
            print('消费者线程开始消费线程了')
            msg=q.get()       #默认阻塞
            print('消费线程得到了数据：{}'.format(msg))
            time.sleep(2)

if __name__ == '__main__':
    t1=Producer()

    t2=Consumer()
    t1.start()
    t2.start()
