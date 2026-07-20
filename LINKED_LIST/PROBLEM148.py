#SORT LIST (LINKED LIST IN ASCENDING ORDER)

from typing import List, Optional
from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#MAIN FUNCTION: SORT LINKED LIST
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #BASE CASE:
        #EMPTY LIST OR ONE NODE IS ALREADY SORTED
        if not head or not head.next:
            return head
        #FIND MIDDLW OF THE LINKED LIST
        slow=head
        fast=head.next
        #SLOW POINTER MOVES 1 STEP 
        #FAST POINTER MOVES 2 STEPS
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #SPLIT THE LIST
        mid=slow.next    #START OF SECOND HALF
        slow.next=None   #BREAK THE LIST INTO TWO HALVES
        #RECURSIVELY SORT LEFT HALF
        left=self.sortList(head)
        #RECURSIVELY SORT RIGHT HALF
        right=self.sortList(mid)
        return self.merge(left,right)
    #MERGE TRWO SORTED LINKED LIST
    def merge(self,left,right):
        #DUMMY NODE TO BUILD MERGED LIST
        dummy=ListNode(0)
        #TAIL ALWAYS POINTS TO LAST NODE
        tail=dummy 
        #COMPARE BOTH THE LISTS
        while left and right:
            #LEFT NODE IS SMALLER 
            if left.val<right.val:
                #ATTACH LEFT NODE
                tail.next=left
                #MOVE LEFT POINTER
                left=left.next
            #RIGHT NODE IS SMALLER OR EQUAL
            else:
                #ATTACH RIGHT NODE
                tail.next=right
                #MOVE RIGHT POINTER
                right=right.next
        #MOVE TAIL TO NEWLY ADDED NIODE
            tail=tail.next
        #ATTACH RAMAINING LEFT NODES
        if left:
            tail.next=left
        #ATTACH RAMAINING RIGHT NODE
        if right:
            tail.next=right
        #RETURN HEAD OF MERGED LIST 
        return dummy.next
#CREATE LINEKD LIST
def createLinkedList(arr):
    if not arr:
        return None
    head=ListNode(arr[0])
    current=head
    for value in arr[1:]:
        current.next=ListNode(value)
        current=current.next
    return head
#PRINT LINKED LIST
def printedLinkedList(head):
    current=head
    while current:
        print(current.val,end=" -> ")
        current=current.next
    print("None")
arr=[4,3,2,1]
head=createLinkedList(arr)
print("ORIGINAL LIST:")
printedLinkedList(head)
obj=Solution()
sorted_head=obj.sortList(head)
print("SORTED LINKED LIST")
printedLinkedList(sorted_head)