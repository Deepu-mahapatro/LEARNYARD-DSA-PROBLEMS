#DINNER PLATES STACKS 

import heapq
class DinnerPlates:
    def __init__(self, capacity: int):
        # MAXIMUM NUMBER OF PLATES
        # EACH STACK CAN HOLD
        self.capacity = capacity
        # STORES ALL THE STACKS
        # EACH ELEMENT IS AN INDIVIDUAL STACK
        self.stacks = []
        # MIN-HEAP
        # STORES INDICES OF STACKS
        # THAT HAVE SPACE
        self.available = []
    def push(self, val: int) -> None:
        # REMOVE FULL STACK INDICES
        # FROM THE MIN-HEAP
        while self.available:
            # GET THE LEFTMOST AVAILABLE STACK
            index = self.available[0]
            # CHECK IF THE STACK IS FULL
            if len(self.stacks[index]) == self.capacity:
                # REMOVE THE FULL STACK
                # FROM THE AVAILABLE HEAP
                heapq.heappop(self.available)
            else:
                # FOUND A STACK WITH SPACE
                break
        # IF THERE IS AN AVAILABLE STACK
        if self.available:
            # GET THE LEFTMOST AVAILABLE STACK
            index = self.available[0]
        else:
            # ALL EXISTING STACKS ARE FULL
            # CREATE A NEW STACK
            index = len(self.stacks)
            self.stacks.append([])
        # PUSH THE VALUE INTO THE STACK
        self.stacks[index].append(val)
        # CHECK IF THE STACK STILL HAS SPACE
        if len(self.stacks[index]) < self.capacity:
            # KEEP THE STACK INDEX
            # IN THE MIN-HEAP
            heapq.heappush(self.available, index)
    def pop(self) -> int:
        # START FROM THE RIGHTMOST STACK
        index = len(self.stacks) - 1
        # MOVE LEFT WHILE THE STACK IS EMPTY
        while index >= 0 and not self.stacks[index]:
            index -= 1
        # IF ALL STACKS ARE EMPTY
        if index < 0:
            # NOTHING TO POP
            return -1
        # REMOVE THE TOP PLATE
        val = self.stacks[index].pop()
        # RETURN THE REMOVED PLATE
        return val
    def popAtStack(self, index: int) -> int:
        # CHECK IF THE STACK INDEX EXISTS
        if index >= len(self.stacks):
            # STACK DOES NOT EXIST
            return -1
        # CHECK IF THE STACK IS EMPTY
        if not self.stacks[index]:
            # NOTHING TO POP
            return -1
        # REMOVE THE TOP PLATE
        val = self.stacks[index].pop()
        # THIS STACK NOW HAS SPACE
        # ADD ITS INDEX TO THE MIN-HEAP
        heapq.heappush(self.available, index)
        # RETURN THE REMOVED PLATE
        return val
    
# CREATE OBJECT
obj = DinnerPlates(2)
# PUSH VALUES
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
# CHECK STACKS
print("Stacks after push:")
print(obj.stacks)
# POP FROM SPECIFIC STACK
result = obj.popAtStack(0)
print("popAtStack(0):", result)
# CHECK STACKS
print("Stacks after popAtStack:")
print(obj.stacks)
# PUSH AGAIN
obj.push(6)
print("Stacks after push(6):")
print(obj.stacks)
# POP FROM RIGHTMOST NON-EMPTY STACK
result = obj.pop()
print("pop():", result)
# FINAL STACKS
print("Final stacks:")
print(obj.stacks)