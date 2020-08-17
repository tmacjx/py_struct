"""
# @Time    : 2020/8/17 15:50
# @Author  : tmackan
"""
import threading
import queue
import random
import time


# Queue自带
# not_full条件锁
# not_empty条件锁


class Producer(threading.Thread):
    def __init__(self, integers, queue):
        super(Producer, self).__init__()
        self.integers = integers
        self.queue = queue

    def run(self):
        while 1:
            integer = random.randint(0, 256)
            self.queue.put(integer)
            print("%d put to queue by %s" % (integer, self.name))
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, integers, queue):
        super(Consumer, self).__init__()
        self.integers = integers
        self.queue = queue

    def run(self):
        while 1:
            integer = self.queue.get()
            print("%d popped by %s" % (integer, self.name))
            self.queue.task_done()


if __name__ == "__main__":
    integer = []
    queue = queue.Queue()
    t1 = Producer(integer, queue)
    t2 = Consumer(integer, queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
