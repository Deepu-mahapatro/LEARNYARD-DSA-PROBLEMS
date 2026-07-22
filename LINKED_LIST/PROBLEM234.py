#PALINDROME IN LINKED LIST

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):

        # Empty or single node
        if not head or not head.next:
            return True

        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None

        while slow:
            # Save next node
            temp = slow.next

            # Reverse link
            slow.next = prev

            # Move prev
            prev = slow

            # Move slow
            slow = temp

        # Compare both halves
        left = head
        right = prev

        while right:

            # Mismatch found
            if left.val != right.val:
                return False

            # Move both pointers
            left = left.next
            right = right.next

        return True


# -----------------------------
# Create Linked List
# -----------------------------
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# -----------------------------
# Print Linked List
# -----------------------------
def printLinkedList(head):

    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# -----------------------------
# Driver Code
# -----------------------------
arr = list(map(int, input("Enter linked list elements: ").split()))

head = createLinkedList(arr)

print("\nLinked List:")
printLinkedList(head)

obj = Solution()

result = obj.isPalindrome(head)

print("\nIs Palindrome:", result)