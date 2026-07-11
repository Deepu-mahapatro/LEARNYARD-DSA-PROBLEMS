#NUMBER OF SUB ARRAYS WITH BOUNDED MAXIMUM

from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        #LAST INDEX WHERE ELEMENT >RIGHT
        last_invalid=-1
        #LAST INDEX WHERE LEFT<= ELEMENT <= RIGHT
        last_valid=-1
        #TOTAL VALID SUB ARRAYS
        count=0
        #TRAVERSE EVERY ELEMENT
        for i in range(len(nums)):
            #ELEMENT IS TOO LARGE 
            #ANY SUB ARRAY CONTAINING IT BECOMES INVALID
            if nums[i]>right:
                last_invalid=i
            #ELEMENT CAN BE THE MAXIMUM OF A VALID SUBARRAY
            if left<=nums[i]<=right:
                last_valid=i
            #COUNT VALID SUBARRAYS ENDING AT INDEX I
            count += max(0,last_valid-last_invalid)
        return count
obj=Solution()
nums=[2,1,4,3]
left=2
right=3
print(obj.numSubarrayBoundedMax(nums,left,right))