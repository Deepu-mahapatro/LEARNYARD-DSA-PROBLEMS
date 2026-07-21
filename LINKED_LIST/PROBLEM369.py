#ADD 1 TO A LINKED LIST 

from typing import List,Optional
# ----------------------------------------
# Definition for Singly Linked List Node
# ----------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val          # Store digit
        self.next = next        # Pointer to next node


class Solution:

    def addOne(self, head):

        # -----------------------------
        # Step 1: Create Dummy Node
        # Handles cases like 9->9->9
        # -----------------------------
        dummy = ListNode(0)
        dummy.next = head

        # Assume dummy is the last non-9 initially
        last_non_nine = dummy

        current = head

        # -----------------------------------
        # Step 2: Find Rightmost Non-9 Digit
        # -----------------------------------
        while current:

            if current.val != 9:
                last_non_nine = current

            current = current.next

        # -----------------------------
        # Step 3: Add One
        # -----------------------------
        last_non_nine.val += 1

        # ----------------------------------------
        # Step 4: Make all digits after it = 0
        # ----------------------------------------
        current = last_non_nine.next

        while current:
            current.val = 0
            current = current.next

        # ----------------------------------------
        # Step 5: Return Answer
        # If dummy became 1, return dummy
        # Otherwise return original head
        # ----------------------------------------
        if dummy.val == 1:
            return dummy

        return dummy.next


# ----------------------------------------
# Create Linked List From Input
# ----------------------------------------
def create_linked_list(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ----------------------------------------
# Print Linked List
# ----------------------------------------
def print_linked_list(head):

    current = head

    while current:

        print(current.val, end="")

        if current.next:
            print(" -> ", end="")

        current = current.next

    print()


# ----------------------------------------
# Main Function
# ----------------------------------------
if __name__ == "__main__":

    # Take input
    arr = list(map(int, input("Enter digits separated by space: ").split()))

    # Create linked list
    head = create_linked_list(arr)

    print("\nOriginal Linked List:")
    print_linked_list(head)

    # Add One
    solution = Solution()
    head = solution.addOne(head)

    print("\nAfter Adding One:")
    print_linked_list(head)