#LINKED LIST RANDOM NODE 

import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head):
        # STORE THE HEAD SO THAT GETRANDOM() CAN
        # TRAVERSE THE LINKED LIST ANYTIME
        self.head = head

    def getRandom(self):
        # BEGIN TRAVERSAL FROM THE FIRST NODE
        current = self.head

        # STORES THE CURRENT RANDOMLY SELECTED VALUE
        answer = None

        # NUMBER OF NODES VISITED SO FAR
        count = 1

        # VISIT EVERY NODE EXACTLY ONCE
        while current:

            # GENERATE A RANDOM NUMBER BETWEEN 1 AND COUNT (INCLUSIVE)
            # REPLACE THE ANSWER ONLY WHEN THE RANDOM NUMBER IS 1
            # THIS GUARANTEES EVERY NODE HAS AN EQUAL PROBABILITY OF SELECTION
            if random.randint(1, count) == 1:
                answer = current.val

            # MOVE TO THE NEXT NODE
            current = current.next

            # INCREASE THE NUMBER OF VISITED NODES
            count += 1

        # RETURN THE RANDOMLY SELECTED NODE VALUE
        return answer


# CREATE A LINKED LIST
def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ---------------- DRIVER CODE ----------------

values = [10, 20, 30, 40, 50]

head = create_linked_list(values)

obj = Solution(head)

print("Random Node Values:\n")

# CALL getRandom() MULTIPLE TIMES
for i in range(10):
    print(obj.getRandom())