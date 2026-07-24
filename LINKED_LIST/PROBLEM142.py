#LINKED LIST CYCLE II

# -----------------------------------------
# Node Definition
# -----------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# -----------------------------------------
# Solution Class
# -----------------------------------------
class Solution:

    def detectCycle(self, head):

        # If list is empty or has only one node
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head

        # -------------------------------
        # Phase 1 : Detect Cycle
        # -------------------------------
        while fast and fast.next:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

            # If they meet, cycle exists
            if slow == fast:

                # -------------------------------
                # Phase 2 : Find Start of Cycle
                # -------------------------------

                # Start pointer from head
                start = head

                # Move both one step at a time
                while start != slow:
                    start = start.next
                    slow = slow.next

                # Found starting node
                return start

        # No cycle
        return None


# -----------------------------------------
# User Input
# -----------------------------------------

n = int(input("Enter number of nodes: "))

values = list(map(int, input("Enter node values: ").split()))

# Create all nodes
nodes = []

for value in values:
    nodes.append(ListNode(value))

# Connect all nodes
for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

# -----------------------------------------
# Create Cycle
# -----------------------------------------
print()
print("Enter cycle position")
print("-1 means No Cycle")
print("0 means First Node")
print("1 means Second Node")
print("2 means Third Node")
print()

pos = int(input("Enter position: "))

# If cycle exists
if pos != -1:
    nodes[-1].next = nodes[pos]

# Head of linked list
head = nodes[0]

# -----------------------------------------
# Find Cycle Start
# -----------------------------------------
obj = Solution()

answer = obj.detectCycle(head)

# -----------------------------------------
# Output
# -----------------------------------------
if answer:
    print("\nCycle starts at node:", answer.val)
else:
    print("\nNo Cycle Found")