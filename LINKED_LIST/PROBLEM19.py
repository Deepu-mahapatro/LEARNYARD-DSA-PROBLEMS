#REMOVE NTH NODE FORM THE END OF THE LINKED LIST

# Node of linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        # Create a dummy node
        dummy = ListNode(0)

        # Connect dummy to head
        dummy.next = head

        # Both pointers start here
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both pointers together
        while fast.next:

            # Move slow one step
            slow = slow.next

            # Move fast one step
            fast = fast.next

        # Skip nth node from end
        slow.next = slow.next.next

        # Return updated list
        return dummy.next


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

# Read number of nodes
size = int(input("Enter number of nodes: "))

# Read node values
arr = list(map(int, input("Enter node values: ").split()))

# Read n value
n = int(input("Enter n: "))

# Create linked list
head = createLinkedList(arr)

print("\nOriginal Linked List:")
printLinkedList(head)

# Remove nth node from end
solution = Solution()
head = solution.removeNthFromEnd(head, n)

print("\nLinked List After Removing Nth Node From End:")
printLinkedList(head)