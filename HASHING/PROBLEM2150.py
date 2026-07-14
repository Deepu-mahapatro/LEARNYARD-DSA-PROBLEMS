#TO FIND ALL LONELY NUMBERS IN AN ARRAY

from typing import List
from collections import Counter 
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        #COUNT HOW MANY TIMES EACH NUMBER APPEARS
        freq=Counter(nums)
        #STORE ALL LONELY NUMBERS
        result=[]
        #CHECK EVERY NUMBER IN THE ORIGINAL ARRAY
        for num in nums:
            #A NUMBER IS LONELY IF :
            #IT APPEARS EXACTLY ONCE
            #NUM-1 IS NOT PRESENT
            #NUM+1 IS NOT PRESENT 
            if (
                freq[num]==1 and
                (num-1) not in freq and 
                (num+1) not in freq
            ):
                result.append(num)
        return result
obj=Solution()
nums=[10,6,8,4]
print(obj.findLonely(nums))