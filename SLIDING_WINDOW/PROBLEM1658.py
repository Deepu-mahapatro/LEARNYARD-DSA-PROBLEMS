#MINIMUM OPERATIONS TO REDUCE X TO ZERO 

from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #CALCULATE TOTAL SUM OF THE ARRAY
        total_sum=sum(nums)
        #SUM THAT SHOULD REMAIN AFTER REMOVING ELEMENTS
        target=total_sum-x
        #IF TARGET BECOMES NEGATIVE
        #X IS GREATER THAN THE TOTAL SUM, SO IMPOSSIBLE
        if target<0:
            return -1
        #SPECIAL CASE:
        #IF TARGET IS 0, WE MUST REMOVE EVERY ELEMENT
        if target==0:
            return len(nums)
        #LEFT POINTER OF SLIDING WINDOW
        left=0
        #CURRENT WINDOW SUM
        window_sum=0
        #STORES THE LENGTH OF THE LONGEST VALID SUB ARRAY
        longest=-1
        #EXPAND THE SLIDING WINDOW
        for right in range(len(nums)):
            #INCLUDE CURRENT ELEMENT IN WINDOW
            window_sum+=nums[right]
            #IF WINDOW SUM BECOMES LARGER THAN TARGET,
            #SHRINK THE WINDOW FROM THE LEFT
            while left<=right and window_sum>target:
                window_sum-=nums[left]
                left+=1
            #CHECK IF CURRENT WINDOW SUM EQUALS TARGET
            if window_sum==target:
                longest=max(longest,right-left+1)
        #NO VALID SUB ARRAY FOUND
        if longest==-1:
            return -1
        #MINIMUM OPERATIONS=TOTAL ELEMENTS-LONGEST SUB ARRAY KEPT
        return len(nums)-longest
nums=[1,1,4,2,3]
x=5
obj=Solution()
print(obj.minOperations(nums,x))