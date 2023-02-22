#!/usr/bin/env python3
"""
atds.py
Data Structures for the Adanced Topics class
Created a stack class in this program.
Created a queue class in this program.
"""

__author__ = "Edward Lee"
__version__ = "2-13-23"


class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return super().__repr__() + self.stack


class Queue(object):
    def __init__(self):
        self.q = []
    
    def enqueue(self,item):
        self.q.append(item)
    
    def dequeue(self):
        return self.q.pop(0)
    
    def peek(self):
        return self.q[0]
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def __str__(self):
        return "Queue" + str(self.q) 


class Deque(object):
    def __init__(self):
        self.deque = []
    
    def addFront(self,item):
        return self.deque.insert(0,item)
    
    def addRear(self,item):
        return self.deque.append(item)
    
    def removeFront(self):
        return self.deque.pop(0)
    
    def removeRear(self):
        return self.deque.pop(len(self.deque) - 1)
    
    def size(self):
        return len(self.deque)
    
    def isEmpty(self):
        return len(self.deque) == 0