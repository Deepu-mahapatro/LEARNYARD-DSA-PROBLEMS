#MAXIMUM ERASURE VALUE

from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #START OF THE CURRENT WINDOW
        left=0
        #END OF THE CURRENT WINDOW (RIGHT)
        #STORES UNIQUE ELEMENTS CURRENTLY PRESENT IN THE WINDOW
        seen=set()
        #SUM OF THE CURRENT UNIQUE WINDOW
        current_sum=0
        #MAXIMUM UNIQUE SUB ARRAY SUN FOUND
        max_sum=0
        #TRAVERSE TEH ARRAY USING THE RIGHT POINTER
        for right in range(len(nums)):
            #IF A DUPLICATE ELEMENT IS FOUND
            #SHIRNK THE WINDOW UNTIL IT BECOMES UNIQUE
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum-=nums[left]
                left+=1
            #ADD THE CURRENT ELEMENT TO THE WINDOW
            seen.add(nums[right])
            current_sum+=nums[right]
            #UPDATE TEH MAXIMUM SUM
            max_sum=max(max_sum,current_sum)
        return max_sum
nums=[4,2,4,5,6]
obj=Solution()
print(obj.maximumUniqueSubarray(nums))