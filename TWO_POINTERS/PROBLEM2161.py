#PARTITION ARRAY ACCORDING TO GIVEN PIVOT

from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result=[]
        #ELEMENTS SMALLER THAN PIVOT
        for num in nums:
            if num<pivot:
                result.append(num)
        #ELEMENTS EQUAL TO PIVOT
        for num in nums:
            if num==pivot:
                result.append(num)
        #ELEMENTS LARGER THAN PIVOT
        for num in nums:
            if num>pivot:
                result.append(num)
        return result
obj=Solution()
nums=[9,12,5,10,14,3,10]
pivot=10
print(obj.pivotArray(nums,pivot))
        
           