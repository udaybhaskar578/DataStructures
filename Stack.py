'''
Author: Sai Uday Bhaskar Mudivarty
Program: Stack
'''
class Stack:
    def __init__(self):
        self.items = list()
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(5)
    stack.push(10)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print(stack.isEmpty())