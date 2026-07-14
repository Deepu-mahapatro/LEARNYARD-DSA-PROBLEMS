#COUNT OF INTERESTING SUB ARRAYS

from typing import List
from typing import List
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        #FREQUENCY MAP FOR PREFIX REMAINDERS
        freq=defaultdict(int)
        #EMPTY PREFIX
        freq[0]=1
        #PREFIX COUNT OF ELEMENTS SATISFYING NUMS[I]%MODULO == K
        prefix=0
        #STORES THE FINAL ANSWER 
        answer=0
        #TRAVERSE IN THE ARRAY
        for num in nums:
            #INCREASE PREFIX COUNT IF CURRENT ELEMENT SATISFIES THE CONDITION
            if num % modulo==k:
                prefix+=1
            #CURRENT PREFIC REMAINDER
            current = prefix % modulo
            #REQUIRED PREVIOUS REMAINDER
            required = (current-k) % modulo
            #ADD THE NUMBER OF VALID PREVIOUS PREFIXES
            answer+=freq[required]
            #STORE CURRENT REMAINDER
            freq[current]+=1
        return answer
obj=Solution()
nums=[2,4,6,1]
modulo=2
k=0
print(obj.countInterestingSubarrays(nums,modulo,k))