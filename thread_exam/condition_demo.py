"""
# @Time    : 2020/8/17 14:03
# @Author  : tmackan
"""


import threading
import random
import time


# 因为生产者和消费者 共同操作一个queue，所以需要锁来控制并发，来判断是写入还是读取
# Condition场景适合
# 生产者 主动休眠
# 消费者 被动通知
class Producer(threading.Thread):
    def __init__(self, integers, condition):
        super(Producer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        while 1:
            integer = random.randint(0, 256)
            # 获取条件锁
            self.condition.acquire()
            print("condition acquired by %s" % self.name)
            self.integers.append(integer)
            # 通知消费者
            print("condition noticed by %s" % self.name)
            self.condition.notify()
            # 释放条件锁
            print("condition release by %s" % self.name)
            self.condition.release()
            # 主动休眠
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, integers, condition):
        super(Consumer, self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        while 1:
            # 获取条件锁
            self.condition.acquire()
            print("condition acquired by %s" % self.name)
            while 1:
                # 如果商品存在，则消费
                if self.integers:
                    integer = self.integers.pop()
                    print("%d popped from list by %s" % (integer, self.name))
                    break
                # 如果不存在，则阻塞当前线程 等待被唤醒
                # wait 实际内存保存了一个wait锁，
                # 首先获取wait锁，释放condition锁，然后阻塞自身
                # 当notify被唤起后, 重新获取condition锁
                print("condition wait by %s" % self.name)
                self.condition.wait()
            print("condition release by %s" % self.name)
            self.condition.release()


if __name__ == "__main__":
    # integers和condition属于线程共享变量
    # 在多进程中需要控制并发访问
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)

    t1.start()
    t2.start()
    t1.join()
    t2.join()




