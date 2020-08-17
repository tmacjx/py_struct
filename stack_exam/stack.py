"""
# @Author  wk
# @Time 2019/8/3 15:17

"""


class Stack(object):
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        self._items.pop()

    def size(self):
        return len(self._items)

    def is_empty(self):
        # if self.size() > 0:
        #     return False
        # else:
        #     return True
        return self._items == []

    def peek(self):
        return self._items[len(self._items) - 1]
