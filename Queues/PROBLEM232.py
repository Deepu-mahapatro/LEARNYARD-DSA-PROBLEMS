#IMPLEMENT QUEUE USING STACKS 

class MyQueue:
    def __init__(self):
        #CREATE TWO STACKS
        #INPUT STACK STORES THE NEW ELEMENTS
        #OUTPUT STACK STORES ELEMENTS FOR POPPING 
        self.input_stack=[]
        self.output_stack=[]
    #PUSH OPERATION
    def push(self,x):
        #ADD NEW ELEMENT TO THE INPUT STACK 
        self.input_stack.append(x)
    #POP OPERATION
    def pop(self):
        #IF THE OUTPUT STACK IS EMPTY MOVE ALL ELEMENTS FORM INPUT STACK TO OUTPUT STACK 
        if not self.output_stack:
            while self.input_stack:
                #MOVE TOP ELEMENT FROM INPUT STACK TO OUTPUT STACK 
                self.output_stack.append(self.input_stack.pop())
        #REMOVE AND RETURN THE FRONT ELEMENT 
        #THE TOP OF THE OUTPUT STACK REPRESENTS THE FRONT OF THE QUEUE
        return self.output_stack.pop()
    #PEEK OPERATION
    def peek(self):
        #IF THE OUTPUT STACK IS EMPTY MOVE ALL ELEMENTS FORM INPUT STACK TO OUTPUT STACK 
        if not self.output_stack:
            while self.input_stack:
                #MOVE THE TOP ELEMENT FROM INPUT STACK TO OUTPUT STACK 
                self.output_stack.append(self.input_stack.pop())
        #RETURN THE FRONT ELEMENT WITHOUT REMOVING IT 
        return self.output_stack[-1]
    #EMPTY OPERATION
    def empty(self):
        #RETURN TRUE ONLY IF THE BOTH STACKS ARE EMPTY 
        return not self.input_stack and not self.output_stack
obj = MyQueue()

obj.push(1)
obj.push(2)
obj.push(3)

print("Peek:", obj.peek())
print("Pop:", obj.pop())
print("Peek:", obj.peek())
print("Pop:", obj.pop())
print("Pop:", obj.pop())
print("Is Empty:", obj.empty())