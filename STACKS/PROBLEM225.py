#IMPLEMENT STACK USING QUEUES

from collections import deque
class MyStack:
    def __init__(self):
        #MAIN QUEUE
        self.q1=deque()
        #TEMPORARY QUEUE
        self.q2=deque()
    def push(self, x: int)-> None:
        #ADD THE NEW ELEMENT TO THE TEMPORARY QUEUE
        self.q2.append(x)
        #MOVE ALL EXISTING ELEMENTS FROM Q1 TO Q2 
        #THIS PUTS THE NEW ELEMENT AT FRONT 
        while self.q1:
            self.q2.append(self.q1.popleft())
        #SWAP Q1 AND Q2
        #NOW Q1 CONTAINS THE STACK IN CORRECT ORDER 
        self.q1,self.q2=self.q2,self.q1
    def pop(self) -> int:
        #REMOVE AND RETURN THE FRONT ELEMENT
        #THE FORNT ELEMENT IS THE TOP OF OUR STACK 
        return self.q1.popleft()
    def top(self) -> int:
        #RETURN THE FRONT ELEMENT WITHOUT REMOVING IT 
        return self.q1[0]
    def empty(self) -> bool:
        #RETURN TRUE IS Q1 IS EMPTY 
        return len(self.q1)==0
# Create a stack object
myStack = MyStack()

# Push elements
myStack.push(1)
myStack.push(2)

# Get the top element
print("Top:", myStack.top())

# Remove the top element
print("Pop:", myStack.pop())

# Get the top element again
print("Top:", myStack.top())

# Check whether the stack is empty
print("Empty:", myStack.empty())

