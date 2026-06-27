#SORT COLORS (0'S 1'S 2'S)

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #EDGE CASE: EMPTY ARRAY
        if len(nums)==0:
            return 0
        #LOW POINTER-> NEXT POSITION FOR 0
        low=0
        #MID POINTER-> CURRENT ELEMENT
        mid=0
        #HIGH POINTER-> NEXT POSITION FOR 2
        high=len(nums)-1
        #TRAVERSE UNTIL MID CROSS THE HIGH
        while mid<=high:
            #IF CURRENT ELEMENT IS ZERO
            if nums[mid]==0:
                #SWAP WITH LOW POINTER
                nums[low],nums[mid]=nums[mid],nums[low]
                #MOVE BOTH POINTER FORWARD
                low+=1
                mid+=1
            #IF CURRENT ELEMENT IS 1
            elif nums[mid]==1:
                #1 IS ALREADY IN CORRECT POSITION
                mid+=1
            #IF CURRENT ELEMENT IS2
            else:
                #SWAP WITH HIGH POINTER
                nums[mid],nums[high]=nums[high],nums[mid]
                #MOVE THE HIGH POINTER BACKWARD
                high-=1
                #DO NOT MOVE MID BECAUSE TEH SWAPPED ELEMENT NEEDS TO BE CHECKED AGAIN
        return nums
obj=Solution()
nums=[2,0,2,1,1,0]
print(obj.sortColors(nums))
        