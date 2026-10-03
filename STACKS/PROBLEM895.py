#MAXIMUM FREQUENCY STACK 

from collections import defaultdict
class FreqStack:
    def __init__(self):
        # STORES HOW MANY TIMES EACH VALUE APPEARS
        self.frequency = {}
        # STORES VALUES GROUPED BY THEIR FREQUENCY
        # group[frequency] = stack of values
        self.group = defaultdict(list)
        # STORES THE HIGHEST FREQUENCY
        self.max_freq = 0
    def push(self, val: int) -> None:
        # INCREASE THE FREQUENCY OF THE VALUE
        freq = self.frequency.get(val, 0) + 1
        self.frequency[val] = freq
        # UPDATE THE HIGHEST FREQUENCY
        self.max_freq = max(self.max_freq, freq)
        # ADD THE VALUE TO THE STACK
        # CORRESPONDING TO ITS NEW FREQUENCY
        self.group[freq].append(val)
    def pop(self) -> int:
        # GET THE MOST RECENT VALUE
        # FROM THE HIGHEST FREQUENCY STACK
        val = self.group[self.max_freq].pop()
        # DECREASE ITS FREQUENCY
        self.frequency[val] -= 1
        # IF THIS FREQUENCY STACK BECOMES EMPTY
        # DECREASE THE MAXIMUM FREQUENCY
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        # RETURN THE REMOVED VALUE
        return val
    
# -----------------------------
# TEST IN VS CODE
# -----------------------------

stack = FreqStack()

stack.push(5)
stack.push(7)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(5)

print(stack.pop())  # 5
print(stack.pop())  # 7
print(stack.pop())  # 5
print(stack.pop())  # 4