"""
# @Author  wk
# @Time 2019/8/3 15:28


  (()()()())
  判断左右括号匹配

"""

from .stack import Stack


def par_checker(symbol_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbol_string) and balanced:
        item = symbol_string[index]
        if item == '(':
            s.push(item)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False
