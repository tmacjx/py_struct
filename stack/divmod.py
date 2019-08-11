"""
# @Author  wk
# @Time 2019/8/11 22:09

    进制转化
"""

from .stack import Stack


def divideBy2(decNumber):

    remstack = Stack()

    while(decNumber > 0):
        rem = decNumber // 2
        remstack.push(rem)
        decNumber = decNumber / 2

    binString = ''
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while (decNumber > 0):
        rem = decNumber // base
        remstack.push(rem)
        decNumber = decNumber / base

    newString = ''
    while not remstack.is_empty():
        newString = newString + digits[remstack.pop()]

    return newString
