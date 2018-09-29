'''
Python 数组实现栈
'''

'''
实现一个栈，getMin方法 O(1)
'''
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]


    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

from collections import deque
queue = deque()

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

'''
用两个队列实现栈
'''
class TwoQueueStack:
    data = deque()
    help = deque()
    data.append()


'''
用两个栈实现队列
'''
