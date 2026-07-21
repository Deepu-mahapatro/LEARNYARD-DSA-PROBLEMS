#COPY LIST WITH RANDOM POINTER

# ============================================
# Definition for a Node
# ============================================

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


# ============================================
# Solution
# ============================================

class Solution:

    def copyRandomList(self, head):

        # Empty List
        if head is None:
            return None

        # STEP 1
        # A -> B -> C
        #
        # becomes
        #
        # A -> A' -> B -> B' -> C -> C'

        curr = head

        while curr:

            copy = Node(curr.val)

            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        # STEP 2
        # Copy Random Pointer

        curr = head

        while curr:

            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        # STEP 3
        # Separate Both Lists

        curr = head
        copyHead = head.next

        while curr:

            copy = curr.next

            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copyHead


# ============================================
# Print Function
# ============================================

def printList(head):

    curr = head

    while curr:

        random = curr.random.val if curr.random else "NULL"

        print(f"{curr.val} --> Random = {random}")

        curr = curr.next


# ============================================
# MAIN
# ============================================

# A -> B -> C

A = Node("A")
B = Node("B")
C = Node("C")

# Next Pointers

A.next = B
B.next = C

# Random Pointers

A.random = C
B.random = A
C.random = B

head = A

print("Original List")
print("----------------")
printList(head)

solution = Solution()

copyHead = solution.copyRandomList(head)

print("\nCopied List")
print("----------------")
printList(copyHead)