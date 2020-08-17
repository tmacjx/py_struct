"""
# @Author  wk
# @Time 2019/8/11 22:37
    烫手山芋


"""

from queue import Queue


def hotPotato(namelist, num):

    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    while len(queue.size()) > 1:
        for i in range(num):
            # 首先弹出最前面的, 然后再再追加到末尾
            queue.enqueue(queue.dequeue())
        # 每一轮结束后，淘汰最前面的
        queue.dequeue()

    return queue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


