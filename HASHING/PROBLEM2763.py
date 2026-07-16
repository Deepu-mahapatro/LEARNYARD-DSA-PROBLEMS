#SUM OF IMBALANCE NUMBERS OF ALL SUBARRAYS

from typing import List
class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        #LENGTH OF THE ARRAY
        n=len(nums)
        #STORE FINAL ANSWER 
        answer=0
        #TRY EVERY POSSIBLE STARTING INDEX
        for i in range(n):
            #STORES THE ELEMENTS PRESENT IN THE CURRENT SUBARRAY
            seen=set()
            #STORES TEH NUMBER OF CONNECTED SEGMENTS
            imbalance=0
            #EXTEND THE SUBARRAY ONE ELEMENT AT A TIME
            for j in range(i,n):
                #CURRENT ELEMEMT 
                x=nums[j]
                #PROCESS ONLY IF X IS NOT ALREADY PRESENT 
                if x not in seen:
                    #CHECK WHETHER X-1 EXISTS
                    left=(x-1) in seen
                    #CHECK WHETHER X+1 EXISTS
                    right=(x+1) in seen
                    #NEITHER NEIGHBOUR EXISTS
                    #A NEW SEGMENT IS CREATED
                    if not left and not right:
                        imbalance+=1
                    #BOTH NEIGHBOURS EXIST
                    #TWO SEGMENTS MERGE INTO ONE 
                    elif left and right:
                        imbalance-=1
                    #ADD THE CURRENT ELEMENT
                    seen.add(x)
                #CONVERT SEGMENTS INTO IMBALANCE
                #IMBALANCE = SEGMENTS - 1
                answer+=(imbalance-1)
        return answer
obj=Solution()
nums=[2,3,1,4]
print(obj.sumImbalanceNumbers(nums))