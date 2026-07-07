#MAXIMUM SUM OF DISTINCT SUBARRAYS WITH LENGTH K

from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #DICTIONARY TO STORE THE FREQUENCY OF ELEMENTS IN CURRENR WINDOW
        freq={}
        #CURRENT WINDOW SUM
        window_sum=0
        #MAXIMUM SUM OF A VALID WINDOW
        max_sum=0
        #TRAVERSE THE ARRAY
        for i in range(len(nums)):
            #ADD THE CURRENT ELEMENT TO THE WINDOW
            window_sum+=nums[i]
            freq[nums[i]]=freq.get(nums[i],0)+1
            #IF WINDOW BECOMES GREATER THAN K (REMOVE LEFT MOST ELEMENT)
            if i>=k:
                left=nums[i-k]
                #REMOVE ITS VALUE FROM THE WINDOW SUM
                window_sum-=left
                #DECREASE ITS FREQUENCY
                freq[left]-=1
                #REMOVE IT FROM THE DICTIONARY IF ITS FREQUENCY BECOMES ZERO
                if freq[left]==0:
                    del freq[left]
            #WHEN WINDOW SIZE BECOMES EXACTLY K ELEMENTS 
            if i>=k-1:
                #IF ALL ELEMENTS ARE DISTINCT 
                if len(freq)==k:
                    #UPDATE THE MAXIMUM SUM
                    max_sum=max(max_sum,window_sum)
        #RETURN THE MAXIMUM VALID SUM
        return max_sum
nums=[1,5,4,2,9,9,9]
k=3
obj=Solution()
print(obj.maximumSubarraySum(nums,k))
