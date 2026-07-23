#ADD TWO NUMBERS 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        # Create dummy node
        dummy = ListNode(0)

        # Current result pointer
        current = dummy

        # Initialize carry value
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:

            # Get first list value
            value1 = l1.val if l1 else 0

            # Get second list value
            value2 = l2.val if l2 else 0

            # Calculate current sum
            total = value1 + value2 + carry

            # Find current digit
            digit = total % 10

            # Update carry value
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)

            # Move current pointer
            current = current.next

            # Move first pointer
            if l1:
                l1 = l1.next

            # Move second pointer
            if l2:
                l2 = l2.next

        # Return answer list
        return dummy.next


# ------------------------------------
# Create Linked List
# ------------------------------------
def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ------------------------------------
# Print Linked List
# ------------------------------------
def print_linked_list(head):

    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# ------------------------------------
# Driver Code
# ------------------------------------

# Input Lists
list1 = [2, 4, 3]
list2 = [5, 6, 4]

# Create Linked Lists
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)

# Create Solution Object
obj = Solution()

# Add Two Numbers
answer = obj.addTwoNumbers(l1, l2)

# Print Input
print("First Linked List:")
print_linked_list(l1)

print("\nSecond Linked List:")
print_linked_list(l2)

# Print Result
print("\nResult Linked List:")
print_linked_list(answer)