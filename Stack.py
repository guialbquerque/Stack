"""
Here we have the classical Stack algorithm.
Steps:
1 - Define the attributes: capacity, top of my stack, vector of values
2 - Method to verify if the stack is full and other method to verify if is empty.
3 - Method to stack up until we reached the max capacity, we need to verify first if is already full.
4 - Method to unstack, we need first verify if is already empty.
5 - Method to see the top of the stack
"""
import numpy as np


class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.empty(self.__capacity, dtype=int)

    def __Stack_Full(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def __Stack_empty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def Stack_Up(self, value):
        if self.__Stack_Full():
            print("The stack is full!")
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def Unstack(self):
        if self.__Stack_empty():
            print("The stack is empty!")
        else:
            self.__top -= 1

    def view_top(self):
        if self.__top == -1:
            return -1
        else:
            return self.__values[self.__top]


if __name__ == '__main__':        
    stack = Stack(5)

    print(stack.view_top())
    print("---")
    stack.Stack_Up(4)
    print(stack.view_top())
    print("---")
    stack.Stack_Up(6)
    stack.Stack_Up(8)
    stack.Stack_Up(10)
    stack.Stack_Up(12)
    stack.Stack_Up(13)

    print(stack.view_top())
    print("---")

    stack.Unstack()
    print(stack.view_top())
    stack.Unstack()
    print(stack.view_top())
    stack.Unstack()
    print(stack.view_top())
    stack.Unstack()
    print(stack.view_top())
    stack.Unstack()
    stack.Stack_Up(13)
    print(stack.view_top())
