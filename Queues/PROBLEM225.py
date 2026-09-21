#IMPLEMENT A STACK USING QUEUES

from collections import deque
class MyStack:
    #CREATE A QUEUE 
    def __init__(self):
        self.queue=deque()
    #PUSH OPERATION
    def push(self,x):
        #ADD THE FIRST NEW ELEMENT TO THE QUEUE 
        self.queue.append(x)
        #MOVE ALL PREVIOUS ELEMENTS BEHIND THE NEW ELEMENT 
        #(THIS MAKES THE NEWEST ELEMENT COME TO HE FRONT OF THE QUEUE)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    #POP OPERATION
    def pop(self):
        #REMOVE AND RETURN THE FRONT ELEMENT
        #THE FRONT ELEMENT IS THE TOP IOF THE STACK 
        return self.queue.popleft()
    #TOP OPERATION
    def top(self):
        #RETURN THE FRONT ELEMENT WITHOUT REMOVING IT 
        return self.queue[0]
    #EMPTY OPERATION
    def empty(self):
        #CHECK IF THE QUEUE IS EMPTY
        return len(self.queue)==0
obj = MyStack()

obj.push(1)
obj.push(2)
obj.push(3)

print("Top:", obj.top())
print("Pop:", obj.pop())
print("Top:", obj.top())
print("Is Empty:", obj.empty())