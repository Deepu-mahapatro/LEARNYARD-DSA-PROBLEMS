#DELETE THE MIDDLE NODE OF LINKED LIST

# Node of linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):

        # If only one node exists
        if head.next is None:
            return None

        # Previous node of slow
        prev = None

        # Slow finds middle node
        slow = head

        # Fast reaches end quickly
        fast = head

        # Traverse the list
        while fast and fast.next:

            # Save previous node
            prev = slow

            # Move slow one step
            slow = slow.next

            # Move fast two steps
            fast = fast.next.next

        # Skip middle node
        prev.next = slow.next

        # Return updated list
        return head


# Build linked list from input
def createLinkedList(arr):

    # Empty list
    if not arr:
        return None

    # Create first node
    head = ListNode(arr[0])

    # Current pointer
    current = head

    # Create remaining nodes
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Print linked list
def printLinkedList(head):

    # Traverse the list
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next

    print()


# ---------------- Driver Code ----------------

# Read list size
n = int(input("Enter number of nodes: "))

# Read node values
arr = list(map(int, input("Enter node values: ").split()))

# Create linked list
head = createLinkedList(arr)

print("\nOriginal Linked List:")
printLinkedList(head)

# Delete middle node
solution = Solution()
head = solution.deleteMiddle(head)

print("\nLinked List After Deleting Middle Node:")
printLinkedList(head)