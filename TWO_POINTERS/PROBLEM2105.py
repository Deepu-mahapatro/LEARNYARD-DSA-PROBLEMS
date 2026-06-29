#WATERING THE PLANTS || 

from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        #TWO POINTERS 
        left=0
        right=len(plants)-1
        #CURRENT WATER AVAILABLE WITH A AND B
        A=capacityA
        B=capacityB
        #COUNT REFILLS
        refills=0
        #PROCESS UNTIL BOTH POINTERS MEET
        while left<right:
            # FOR A MAN
            #IF A DOES NOT HAVE ENOUGH WATER,REFILL FIRST
            if A<plants[left]:
                refills+=1
                A=capacityA
            #WATER THE CURRENT PLANT
            A-=plants[left]
            left+=1
            #FOR B MAN
            #IF B DOES NOT HAVE ENOUGH WATER,REFILL FIRST
            if B<plants[right]:
                refills+=1
                B=capacityB
            #WATER THE CURRENT PLANT
            B-=plants[right]
            right-=1
        #IF ONE MIDDLE PLANT IS THERE
        if left==right:
            #THE PERSON WITH MORE REMAINING WATER WATERS TEH PALNT
            if A>=B:
                if A<plants[left]:
                    refills+=1
            else:
                if B<plants[left]:
                    refills+=1
        return refills
obj=Solution()
plants=[2,4,5,1,2]
capacityA=5
capacityB=7
print(obj.minimumRefill(plants,capacityA,capacityB))