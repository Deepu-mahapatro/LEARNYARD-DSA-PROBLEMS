#MERGE K SORTED LIST

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        # STEP 1: CREATE A DUMMY NODE
        dummy = ListNode(0)

        # STEP 2: CURRENT POINTER
        current = dummy

        # STEP 3: CREATE AN EMPTY MIN HEAP
        heap = []

        # STEP 4: PUSH THE FIRST NODE OF EVERY LIST
        for index, node in enumerate(lists):

            # IGNORE EMPTY LINKED LISTS
            if node:

                # PUSH (VALUE, INDEX, NODE)
                heapq.heappush(heap, (node.val, index, node))

        # STEP 5: CONTINUE UNTIL HEAP BECOMES EMPTY
        while heap:

            # REMOVE THE SMALLEST NODE
            value, index, node = heapq.heappop(heap)

            # ATTACH THE SMALLEST NODE
            current.next = node

            # MOVE CURRENT POINTER
            current = current.next

            # PUSH THE NEXT NODE OF THE SAME LIST
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        # STEP 6: RETURN THE MERGED LINKED LIST
        return dummy.next


# ----------------------------------------------------
# CREATE A LINKED LIST
# ----------------------------------------------------
def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ----------------------------------------------------
# PRINT A LINKED LIST
# ----------------------------------------------------
def print_linked_list(head):

    current = head

    while current:

        print(current.val, end=" -> ")

        current = current.next

    print("None")


# ----------------------------------------------------
# DRIVER CODE
# ----------------------------------------------------

# CREATE MULTIPLE SORTED LINKED LISTS
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

# STORE ALL HEADS INSIDE A LIST
lists = [list1, list2, list3]

# CREATE OBJECT
obj = Solution()

# MERGE ALL LINKED LISTS
answer = obj.mergeKLists(lists)

# PRINT RESULT
print("Merged Linked List:\n")
print_linked_list(answer)