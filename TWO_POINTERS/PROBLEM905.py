#SORT ARRAY BY PARITY
from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            #IF LEFT SIDE IS EVEN MOVE POINTER STAY SAME
            if nums[l]%2==0:
                l+=1
            #IF RIGHT SIDE IS ODD MOVE POINTER STAY SAME 
            elif nums[r]%2==1:
                r-=1
            #IF IN REVERSE ORDER THEN SWAP THEM AND MOVE THE POINTERS TOWARDS
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        return nums
obj=Solution()
nums=[1,2,3,4,5]
print(obj.sortArrayByParity(nums))
        