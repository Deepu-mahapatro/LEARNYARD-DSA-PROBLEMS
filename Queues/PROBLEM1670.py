#DESIGN FRONT MIDDLE BACK QUEUE

from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        # CREATE TWO DEQUES
        # LEFT STORES THE FIRST HALF
        # RIGHT STORES THE RIGHT HALF
        self.left = deque()
        self.right = deque()

    def balance(self):
        # IF LEFT HAS MORE THAN ONE EXTRA ELEMENT
        # MOVE THE LAST ELEMENT OF LEFT TO FRONT OF RIGHT
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())

        # IF RIGHT HAS MORE ELEMENTS THAN LEFT
        # MOVE THE FIRST ELEMENT OF RIGHT TO THE END OF LIST
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        # ADD THE VALUE TO THE FRONT OF LEFT
        self.left.appendleft(val)

        # BALANCE THE TWO DEQUES
        self.balance()

    def pushMiddle(self, val):
        # IF LEFT HAS ONE MORE ELEMENT THAN RIGHT
        # MOVE THE CURRENT MIDDLE ELEMENT TO FRONT OF RIGHT
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

        # ADD THE VALUE TO THE END OF LEFT
        # THIS PLACES IT IN THE MIDDLE
        self.left.append(val)

        # BALANCE THE TWO DEQUES
        self.balance()

    def pushBack(self, val):
        # ADD THE VALUE TO THE END OF THE RIGHT
        self.right.append(val)

        # BALANCE THE TWO DEQUES
        self.balance()

    def popFront(self):
        # IF THE QUEUE IS EMPTY, RETURN -1
        if not self.left and not self.right:
            return -1

        # REMOVE THE FRONT ELEMENT FROM LEFT
        value = self.left.popleft()

        # BALANCE THE TWO DEQUES
        self.balance()

        return value

    def popMiddle(self):
        # IF THE QUEUE IS EMPTY, RETURN -1
        if not self.left and not self.right:
            return -1

        # REMOVE THE MIDDLE ELEMENT FROM THE END OF LEFT
        value = self.left.pop()

        # BALANCE THE TWO DEQUES
        self.balance()

        return value

    def popBack(self):
        # IF THE QUEUE IS EMPTY, RETURN -1
        if not self.left and not self.right:
            return -1

        # IF RIGHT HAS ELEMENTS,
        # REMOVE THE LAST ELEMENT FROM RIGHT
        if self.right:
            value = self.right.pop()

        # OTHERWISE REMOVE FROM LEFT
        else:
            value = self.left.pop()

        # BALANCE THE TWO DEQUES
        self.balance()

        return value

# TESTING THE QUEUE

obj = FrontMiddleBackQueue()

obj.pushFront(1)
obj.pushBack(2)
obj.pushMiddle(3)
obj.pushMiddle(4)

print(obj.popFront())
print(obj.popMiddle())
print(obj.popMiddle())
print(obj.popBack())
print(obj.popFront())