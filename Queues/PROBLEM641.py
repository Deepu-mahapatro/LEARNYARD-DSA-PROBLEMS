#DESIGN A CIRCULAR DEQUE 

class MyCircularDeque:
    def __init__(self,k):
        #MAXIMUM CAPACITY OF THE DEQUE 
        self.k=k
        #ARRAY TO STORE ELEMENTS 
        self.deque=[0]*k
        #INDEX OF THE FRONT ELEMENT 
        self.front=0
        #CURRENT NUMBER OF ELEMENTS
        self.size=0
    def insertFront(self,value):
        #IF DEQUE IS FULL, INSERTION IS IMPOSSIBLE 
        if self.isFull():
            return False
        #MOVE THE FRONT ONE POSITION BACKWARD %K MAKES THE INDEX CIRCULAR
        self.front=(self.front-1)%self.k
        #STORE THE VALUE AT THE NEW FRONT
        self.deque[self.front]=value
        #INCREASE NUMBER OF ELEMENTS 
        self.size+=1
        return True
    def insertLast(self,value):
        #IF DEQUE IS FULL, INSERTION IS IMPOSSIBLE 
        if self.isFull():
            return False
        #FIND THE POSITION AFTER THE CURRENT REAR
        rear=(self.front+self.size)%self.k
        #INSERT VALUE AT REAR
        self.deque[rear]=value
        #INCREASE NUMBER OF ELEMENTS
        self.size+=1
        return True
    def deleteFront(self):
        #IF DEQUE IS EMPTY, NOTHING TO DELETE
        if self.isEmpty():
            return False
        #MOVE FRONT ONE POSITION FORWARD 
        self.front=(self.front+1)%self.k
        #DECREASE NUMBER OF ELEMENTS
        self.size-=1
        return True
    def deleteLast(self):
        #IF DEQUE IS EMPTY, NOTHING TO DELETE
        if self.isEmpty():
            return False
        #JUST REDUCE THE NUMBER OF ELEMENTS 
        #THE OLD LST POSITION WILL NO LONGER BE PART OF THE DEQUE 
        self.size-=1
        return True
    def getFront(self):
        #IF DEQUE IS EMPTY
        if self.isEmpty():
            return -1
        #FRONT ELEMENT IS AT THE SELF.FRONT
        return self.deque[self.front]
    def getRear(self):
        #IF DEQUE IS EMPTY
        if self.isEmpty():
            return -1
        #FIND THE INDEX OF THE LAST ELEMENT
        rear=(self.front+self.size-1)%self.k
        return self.deque[rear]
    def isEmpty(self):
        #DEQUE IS EMPTY WHEN THE SIZE IS 0
        return self.size==0
    def isFull(self):
        #DEQUE IS FULL WHEN THE SIZE REACHES TO K
        return self.size==self.k
obj = MyCircularDeque(3)

print("insertLast(1):", obj.insertLast(1))
print("insertLast(2):", obj.insertLast(2))
print("insertFront(3):", obj.insertFront(3))

print("getFront():", obj.getFront())
print("getRear():", obj.getRear())

print("insertLast(4):", obj.insertLast(4))

print("isFull():", obj.isFull())

print("deleteFront():", obj.deleteFront())

print("insertLast(4):", obj.insertLast(4))

print("getFront():", obj.getFront())
print("getRear():", obj.getRear())