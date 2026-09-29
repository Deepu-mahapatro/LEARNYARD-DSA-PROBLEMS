#IMPLEMENTING A STACK END TO END 

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def isempty(self):
        return len(self.stack)==0
    def isfull(self):
        return len(self.stack)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())