import numpy as np


class StackValidator:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.chararray(shape=self.__capacity, unicode=True)

    def __Stack_Full(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def Stack_empty(self):
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
        if self.Stack_empty():
            print("The stack is empty!")
        else:
            value = self.__values[self.__top]
            self.__top -= 1
            return value

    def view_top(self):
        if self.__top == -1:
            return -1
        else:
            return self.__values[self.__top]


S = str(input("type one expression \n"))
# a{b(c)}
validator = StackValidator(len(S))
for i in range(len(S)):
    ch = S[i]
    if ch == '{' or ch == '(' or ch == '[':
        validator.Stack_Up(ch)
    elif ch == '}' or ch == ')' or ch == ']':
        if not validator.Stack_empty():
            chx = str(validator.Unstack())
            if (ch == '}' and chx != '{') or (ch == ')' and chx != '(') or (ch == ']' and chx != '['):
                print(f"Error! {ch} in position {i}")
                break

