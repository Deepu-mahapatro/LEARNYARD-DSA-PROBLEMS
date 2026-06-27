#4 SUM

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #SORT THE ARRAY
        nums.sort()
        result=[]
        #FIX TEH FIRST ELEMENT
        for i in range(len(nums)-3):
            #SKIP DUPLICATES FIRST ELEMENTS
            if i>0 and nums[i]==nums[i-1]:
                continue
            #FIX THE SECOND ELEMENT
            for j in range(i+1,len(nums)-2):
                #SKIP THE DUPLICATES SECOND ELEMENTS
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                #LEFT POINTER
                left=j+1
                #RIGHT POINTER
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    #FOUND A QUADRANT
                    if total==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        #SKIP DUPLICATES VALUES ON LEFT
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        #SKIP DUPLICATES VALUES ON RIGHT
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    #IF SUM IS TOO SMALL,MOVE LEFT POINTER
                    elif total<target:
                        left+=1
                    #IF SUM IS TOO LARGE,MOVE RIGHT POINTER
                    else:
                        right-=1
        return result
obj=Solution()
nums=[1,0,-1,0,-2,2]
target=0
print(obj.fourSum(nums,target))