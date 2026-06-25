#REMOVE DUPLICATES FROM SORTED ARRAY

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #EDGE CASE 
        #IF ARRAY IS EMPTY
        if len(nums)==0:
            return 0
        #SLOW POINTER (POINTS TO UNIQUE ELEMENT)
        i=0
        #FAST POINTER
        #TRAVERSE THE ARRAY TO FIND UNIQUE ELEMENTS
        for j in range(1,len(nums)):
            #IF NEW UNIQUE ELEMENT
            if nums[i]!=nums[j]:
                #INCREASE THE POINTER
                i+=1
                #PLACE UNIQUE ELEMENT AT THE SLOW POINTER POSITION
                nums[i]=nums[j]
        return i+1
obj=Solution()
nums=[2,2,3,4]
print(obj.removeDuplicates(nums))