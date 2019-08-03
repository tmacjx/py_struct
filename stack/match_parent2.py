"""
# @Author  wk
# @Time 2019/8/3 15:40

    判断多种括号是否匹配
    [ [ { { ( ( ) ) } } ] ]

    ( ( ( ) ] ) )
"""

from .stack import Stack


def match(open, close):
    opens = '[({'
    closes = '])}'
    return opens.index(open) == closes.index(close)


def par_checker(symbol_string):
    s = Stack()
    index = 0
    balanced = True

    while index < len(symbol_string) and balanced:
        item = symbol_string[index]
        if item in '([{':
            s.push(item)
        else:
            if s.is_empty():
                balanced = False
            top = s.pop()
            if not match(top, item):
                balanced = False
        index = index + 1

    if s.is_empty() and balanced:
        return True
    else:
        return False

