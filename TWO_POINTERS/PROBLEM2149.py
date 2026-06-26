#REARRANGE ELEMENTS BY SIGN 
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        #EVEN INDEX
        pos=0
        #ODD INDEX
        neg=1
        for num in nums:
            #FOR POSITIVE NUMBERS
            if num>0:
                result[pos]=num
                pos+=2
            #FOR NEGATIVE NUMBERS
            else:
                result[neg]=num
                neg+=2
        return result
obj=Solution()
nums=[1,-2,-3,-4,5,-6,7,8]
print(obj.rearrangeArray(nums))