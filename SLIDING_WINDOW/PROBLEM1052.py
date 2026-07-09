#GRUMPY BOOKSTORE PROBLEM

from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #CUSTOMERS ALREADY SATISFIED WITHOUT USING THE TECHNIQUE 
        already_satisfied=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                already_satisfied+=customers[i]
        #CURRENT EXTRA CUSTOMERS IN THE SLIDING WINDOW
        current_extra=0
        #MAXIMUM EXTRA CUSTOMERS FOUND
        max_extra=0
        #TRAVERSE THE ARRAY
        for right in range(len(customers)):
            #ADD CUSTOMERS ONLY IF THE OWNER IS GRUMPY
            if grumpy[right]==1:
                current_extra+=customers[right]
            #REMOVE THE LEFTMOST ELEMENT WHEN THE WINDOW LENGTH EXCEEDS
            if right>=minutes:
                if grumpy[right-minutes]==1:
                    current_extra-=customers[right-minutes]
            #UPDATE MAXIMUM EXTRA CUSTOMERS
            max_extra=max(max_extra,current_extra)
        #TOTAL SATISFIED CUSTOMERS
        return already_satisfied +max_extra
obj=Solution()
customers=[1,0,1,2,1,1,7,5]
grumpy=[0,1,0,1,0,1,0,1]
minutes=3
print(obj.maxSatisfied(customers,grumpy,minutes))