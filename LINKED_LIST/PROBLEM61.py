#ROTATE LINKED LIST BY K TIMES 


# Definition for a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):

        # If list is empty, has only one node,
        # or no rotations are needed
        if not head or not head.next or k == 0:
            return head

        # ------------------------------------
        # STEP 1: Find length of the list
        # and the last node (tail)
        # ------------------------------------
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # ------------------------------------
        # STEP 2: Reduce unnecessary rotations
        # Example:
        # Length = 5
        # k = 8
        # Effective rotations = 8 % 5 = 3
        # ------------------------------------
        k = k % length

        # If rotation becomes 0
        if k == 0:
            return head

        # ------------------------------------
        # STEP 3: Connect tail to head
        # Make the linked list circular
        #
        # 1 -> 2 -> 3 -> 4 -> 5
        # ^                   |
        # |___________________|
        # ------------------------------------
        tail.next = head

        # ------------------------------------
        # STEP 4: Find the new tail
        #
        # New Tail Position:
        # length - k - 1
        #
        # New Head:
        # newTail.next
        # ------------------------------------
        steps = length - k - 1

        newTail = head

        while steps:
            newTail = newTail.next
            steps -= 1

        # ------------------------------------
        # STEP 5: New head is next node
        # ------------------------------------
        newHead = newTail.next

        # ------------------------------------
        # STEP 6: Break the circular list
        # ------------------------------------
        newTail.next = None

        # Return rotated linked list
        return newHead


# ------------------------------------------
# Helper Function
# Create Linked List
# ------------------------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# ------------------------------------------
# Helper Function
# Print Linked List
# ------------------------------------------
def printLinkedList(head):

    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next

    print()


# ------------------------------------------
# Driver Code
# ------------------------------------------

nums = list(map(int, input("Enter linked list elements: ").split()))
k = int(input("Enter k: "))

head = createLinkedList(nums)

solution = Solution()
newHead = solution.rotateRight(head, k)

print("\nRotated Linked List:")
printLinkedList(newHead)