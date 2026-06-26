#SORT ARRAY BY PARITY II
from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return 0
        #EVEN INDEX
        even=0
        #ODD INDEX
        odd=0
        while even<len(nums) and odd<len(nums):
            #CORRECT EVEN NUMBER AT EVEN INDEX
            if nums[even]%2==0:
                even+=2
            #CORRECT ODD NUMBER AT ODD INDEX
            elif nums[odd]%2==1:
                odd+=2
            #WRONG ELEMENTS AT BOTH INDEX->SWAP
            else:
                nums[even],nums[odd]=nums[odd],nums[even]
                even+=2
                odd+=2
        return nums
obj=Solution()
nums=[2,4,6,1,3,5,3]
print(obj.sortArrayByParityII(nums))