#COUNT SUB ARRAYS WITH MEDIAN K

from collections import defaultdict
from typing import List
from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #FIND THE INDEX OF K
        k_index=nums.index(k)
        #STORE BALANCE FREQUENCIES 
        balance_count=defaultdict(int)
        #EMPTY LEFT SIDE HAS BALANCE 0
        balance_count[0]=1
        #CURRENT BALANCE
        balance=0
        #TRAVERSE LEFT OF K
        for i in range(k_index-1,-1,-1):
            #SMALLER THAN K
            if nums[i]<k:
                balance-=1
            #GREATER THAN K
            else:
                balance+=1
            #STORE THSI BALANCE
            balance_count[balance]+=1
        #STORE FINAL ANSWER
        answer=0
        #RESET BALANCE
        balance=0
        #TRAVERSE FROM K TO THE END 
        for i in range(k_index,len(nums)):
            #SMALLER THAN K
            if nums[i]<k:
                balance+=1
            #K DOES NOT CHANGE BALANCE
            #TOTAL BALANCE BECOMES 0
            answer+=balance_count[-balance]
            #TOTAL BALANCE BECOMES 1
            answer+=balance_count[1-balance]
        #RETURN TOTAL VALID SUBARRAYS
        return answer 
obj=Solution()
nums=[3,2,1,4,5]
k=4
print(obj.countSubarrays(nums,k))