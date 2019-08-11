"""
# @Author  wk
# @Time 2019/8/3 16:09

    链表的py实现
"""


class Node(object):
    """
    节点只关心 当前的data和next引用
    如果next为None 则表示无后续节点
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):
    """
    只关心head引用, 不关心实际node
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def append(self):
        pass

    def index(self, item):
        current = self.head

        found = False

        pass

    def insert(self):


        pass

    def pop(self, pos):
        current = self.head
        previous = None
        index = 0
        found = False
        while not found:
            if pos == index:
                found = True
            else:
                index = index + 1
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = None
        else:
            previous.set_next(current.get_next())







