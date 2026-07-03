#NUMBER OF SUB ARRAYS OF SIZE K AND AVERAGE GREATER THAN OR EQUAL TO THRESHOLD 

from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #SUM OF THE CURRENT WINDOW
        window_sum=0
        #COUNT OF VALID SUBARRAYS
        count=0
        #TRAVERSE THE ARRAY
        for i in range(len(arr)):
            #ADD THE CURRENT ELEMENT OF THE WINDOW 
            window_sum+=arr[i]
            #IF WINDOW SIZE BECOMES GREATER THAN K
            #REMOVE THE LEFTMOST ELEMENT
            if i>=k:
                window_sum-=arr[i-k]
            #WHEN SINDOW SIZE BECOMES EXACTLY K
            if i>=k-1:
                #CALCULATE THE AVERAGE OF THE CURRENT WINDOW
                average=window_sum/k
                #IF AVERAGE IS GREATER THAN OR EQUAL TO THERESHOLD 
                if average>=threshold:
                    count+=1
        #RETURN THE TOTAL COUNT
        return count
obj=Solution()
arr=[2,2,2,2,5,5,5,8]
k=3
threshold=4
print(obj.numOfSubarrays(arr,k,threshold))