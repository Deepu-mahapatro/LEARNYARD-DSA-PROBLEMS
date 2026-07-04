#3 SUM CLOSEST

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #SORT THE ARRAY
        nums.sort()
        #ASSUME THE FIRST THREE ELEMENTS FORM THE CLOSEST SUM
        closest_sum=nums[0]+nums[1]+nums[2]
        #FIX ONE ELEMENT T A TIME
        for i in range(len(nums)-2):
            #TWO POINTERS
            left=i+1
            right=len(nums)-1
            #CONTINUE UNITL POINTERS MEET
            while left<right:
                #CURRENT SUM OF THREE NUMBERS
                current_sum=nums[i]+nums[left]+nums[right]
                #UPDATE THE CLOSEST SUM IF CURRENT SUM IS NEARER TO TARGET
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                #PERFECT MATCH FOUND
                if current_sum==target:
                    return current_sum
                #CURRENT SUM IS TOO SMALL
                #INCREASE IT BY MOVING THE LEFT POINTER 
                elif current_sum<target:
                    left+=1
                #CURRENT SUM IS TOO LARGE
                #DECREASE IT BY MOVE THE RIGHT POINTER
                else:
                    right-=1
        return closest_sum
obj=Solution()
nums=[-1,2,1,-4]
target=1
print(obj.threeSumClosest(nums,target))