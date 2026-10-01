#DESIGN A STACK WITH INCREMENT OPERATION 

class CustomStack:
    def __init__(self,maxSize: int):
        #STORE THE MAXIMUM ALLOWED SIZE OF THE STACK
        self.maxSize=maxSize
        #CREATE AN EMPTY STACK 
        self.stack=[]
    def push(self,x: int) -> None:
        #ONLY ADD THE ELEMENT TO THE TOP OF THE STACK 
        if len(self.stack)<self.maxSize:
            #ADD THE ELEMENT TO THE TOP OF THE STACK 
            self.stack.append(x)
    def pop(self) -> int:
        #IF THE STACK IS EMPTY
        if not self.stack:
            return -1
        #REMOVE AND RETURN THE TOP ELEMENT 
        return self.stack.pop()
    def increment(self, k: int, val:int) -> None:
        #WE NEED TO INCREMENT THE BOTTOM K ELEMENTS
        #IF THE K IS GREATER THAN THE NUMBER OF ELEMENTS IN THE STACK 
        #WE CAN ONLY INCREMENT THE ELEMENTS THAT ACTUALLY EXISTS IN THE STACK 
        limit=min(k,len(self.stack))
        #GO THROUGH THE BOTTOM 'LIMIT' ELEMENTS
        for i in range(limit):
            #ADD VAL TO EACH ELEMENT 
            self.stack[i]+=val
            
# Create a stack with maximum size 3
stack = CustomStack(3)

# Push elements
stack.push(1)
stack.push(2)
stack.push(3)

# Stack:
# [1, 2, 3]

# Increment the bottom 2 elements by 100
stack.increment(2, 100)

# Stack becomes:
# [101, 102, 3]

# Pop the top element
print("Pop:", stack.pop())

# Pop the next element
print("Pop:", stack.pop())

# Pop the last element
print("Pop:", stack.pop())

# Try to pop from an empty stack
print("Pop:", stack.pop())