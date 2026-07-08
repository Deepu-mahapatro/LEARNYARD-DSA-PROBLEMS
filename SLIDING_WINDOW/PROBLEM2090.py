from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        #RESULT ARRAY FILLED WITH -1
        result=[-1]*n
        #REQUIRED WINDOW SIZE
        window_size=2*k+1
        #IF WINDOW CANNOT FIT
        if window_size>n:
            return result
        #SUM OF CURRENT WINDOW
        window_sum=0
        #TRAVERSE THE ARRAY
        for i in range(n):
            #ADD TEH CURRENT ELEMENT
            window_sum+=nums[i]
            #REMOVE TH LEFTMOST ELEMENT WHEN WINDOW SIZE EXCEEDS
            if i>=window_size:
                window_sum-=nums[i-window_size]
            #WINDOW HAS EXACTLY REUQIRED SIZE
            if i>=window_size-1:
                #FIND THE CENTER INDEX 
                center=i-k
                #ST0RE FLOOR AVERAGE
                result[center]=window_sum//window_size
        return result
obj=Solution()
nums=[7,4,3,9,1,8,5,2,6]
k=3
print(obj.getAverages(nums,k))