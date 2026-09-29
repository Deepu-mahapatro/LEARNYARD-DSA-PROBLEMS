#IMPLEMENT MIN STACK


class MinStack:
    def __init__(self):
        #MAIN STACK STORES ALL THE ELEMENTS 
        self.stack=[]
        #MIN STACK STORES THE MINIMUM VALUES 
        self.min_stack=[]
    def push(self,val: int) -> None:
        #ADD THE VALUE TO THE MAIN STACK 
        self.stack.append(val)
        #IF MIN_STACK IS EMPTY OR VAL US SMALLER THAN TEH CURRENT MINIMUM WE ADD IT TO MIN_STACK 
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        #REMOVE THE TOP ELEMENT FROM THE MAIN STACK 
        removed=self.stack.pop()
        #IF THE REMOVED ELEMENT IS ALSO THE CURRENT MINIMUM REMOVE IT FROM MIN_STACK 
        if removed==self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        #RETURN THE TOP ELEMENT OF THE MAIN STACK 
        return self.stack[-1]
    def getMin(self) -> int:
        #TOP OF MIN_STACK ALWAYS CONTAINS THE MINIMUM VALUE 
        return self.min_stack[-1]
    
# Create MinStack object
min_stack = MinStack()

# Push elements
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

# Get minimum value
print("Minimum:", min_stack.getMin())

# Remove top element
min_stack.pop()

# Get top element
print("Top:", min_stack.top())

# Get minimum value again
print("Minimum:", min_stack.getMin())