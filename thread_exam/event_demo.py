"""
# @Time    : 2020/8/17 15:36
# @Author  : tmackan
"""

import threading
import random
import time

# Event 事件
# 生产者 主动push event
# 消费者 被动阻塞监听 event


class Producer(threading.Thread):
    def __init__(self, integers, event):
        super(Producer, self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        while 1:
            integer = random.randint(0, 256)
            self.integers.append(integer)
            print("%d append list by  %s" % (integer, self.name))
            print("event set by %s" % self.name)
            # 设置事件
            self.event.set()
            # 发送事件
            self.event.clear()
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, integers, event):
        super(Consumer, self).__init__()
        self.integers = integers
        self.event = event

    def run(self):
        while 1:
            self.event.wait()
            try:
                integer = self.integers.pop()
                print("%d popped by %s" % (integer, self.name))
            except IndexError:
                time.sleep(1)


if __name__ == "__main__":
    integers = []
    # Event 乞丐版的Condition
    # flag标志事件
    event = threading.Event()

    t1 = Producer(integers, event)
    t2 = Consumer(integers, event)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

