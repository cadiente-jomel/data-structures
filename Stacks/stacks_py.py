from collections import deque

# s = deque()

# s.append('john')
# s.append('jane')
# s.append('mark')

# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)

# ! stack prototype
# push pop peek is_empty sizer
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        return self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return print(len(self.container))

s = Stack()

s.push(5)
s.push(1)
s.push(4)
s.size()
print(s.is_empty())
print(s.container)
print(s.peek())
s.pop()
print(s.container)