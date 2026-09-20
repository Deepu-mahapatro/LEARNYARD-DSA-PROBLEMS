#DESIGN A CIRCULAR QUEUE

class MyCircularQueue:

    def __init__(self, k):
        # STORE THE MAXIMUM CAPACITY
        self.k = k

        # CREATE A FIXED-SIZE ARRAY
        self.queue = [0] * k

        # INDEX OF THE FRONT ELEMENT
        self.front = 0

        # NUMBER OF ELEMENTS CURRENT IN THE QUEUE
        self.size = 0

    def enQueue(self, value):
        # IF THE QUEUE IS FULL, INSERTION IS NOT POSSIBLE
        if self.isFull():
            return False

        # CALCULATING THE POSITION FOR THE NEW ELEMENT
        # %K MAKES THE QUEUE CIRCULAR
        rear = (self.front + self.size) % self.k

        # INSERT THE VALUE AT THE CALCULATED POSITION
        self.queue[rear] = value

        # INCREASE THE NUMBER OF ELEMENTS
        self.size += 1

        return True

    def deQueue(self):
        # IF THE QUEUE IS EMPTY, DELETION IS NOT POSSIBLE
        if self.isEmpty():
            return False

        # MOVE THE FRONT TO THE NEXT POSITION
        # %K MAKES IT WRAP AROUND WHEN NEEDED
        self.front = (self.front + 1) % self.k

        # DECREASE THE NUMBER OF ELEMENTS
        self.size -= 1

        return True

    def Front(self):
        # IF THE QUEUE IS EMPTY, RETURN -1
        if self.isEmpty():
            return -1

        # RETURN THE ELEMENT AT FRONT
        return self.queue[self.front]

    def Rear(self):
        # IF THE QUEUE IS EMPTY, RETURN -1
        if self.isEmpty():
            return -1

        # CALCULATE THE INDEX OF THE LAST ELEMENT
        rear = (self.front + self.size - 1) % self.k

        return self.queue[rear]

    def isEmpty(self):
        # QUEUE IS EMPTY WHEN THE SIZE IS 0
        return self.size == 0

    def isFull(self):
        # QUEUE IS FULL WHEN THE SIZE EQUALS TO CAPACITY
        return self.size == self.k


# --------------------------------
# TESTING THE CIRCULAR QUEUE
# --------------------------------

obj = MyCircularQueue(3)

print(obj.enQueue(1))   # True
print(obj.enQueue(2))   # True
print(obj.enQueue(3))   # True
print(obj.enQueue(4))   # False

print(obj.Rear())       # 3
print(obj.isFull())     # True

print(obj.deQueue())    # True
print(obj.enQueue(4))   # True

print(obj.Rear())       # 4
print(obj.Front())      # 2
print(obj.isEmpty())    # False