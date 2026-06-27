#3 SUM

from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #SORT THE ARRAY
        nums.sort()
        result=[]
        #FIX ONE ELEMENT AT A TIME
        for i in range(len(nums)-2):
            #SKIP THE DUPLICATES FIRST ELEMENTS
            if i>0 and nums[i]==nums[i-1]:
                continue
            #LEFT POINTER
            left=i+1
            #RIGHT POINTER
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                #FOUND THE TARGET
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    #SKIP DUPLICATES VALUES ON LEFT 
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    #SKIP DUPLICATES VALUES ON RIGHT
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                #SUM IS TOO SMALL ,MOVE LEFT POINTER'
                elif total<0:
                    left+=1
                #SUM IS TOO LARGE,MOVE RIGHT POINTER
                else:
                    right-=1
        return result
obj=Solution()
nums=[-1,0,1,2,-1,-4]
print(obj.threeSum(nums))