#CONTAINER WITH MOST WATER

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #LEFT POINTER
        left=0
        #RIGHT POINTER
        right=len(height)-1
        #STORE MAXIMUM AREA
        max_area=0
        #CONTINUE UNTIL BOTH POINTERS MEET
        while left<right:
            #CALCULATE WIDTH
            width=right-left
            #CALCULATE BREADTH
            breadth=min(height[left],height[right])
            #AREA=WIDTH*BREADTH
            area=width*breadth
            #UPDATE THE MAXIMUM AREA
            max_area=max(max_area,area)
            #MOVE THE POINTER WITH TEH SMALLER HEIGHT
            if height[left]<height[right]:
                left+=1
            #OTHERWISE MOVE THE RIGHT POINTER
            else:
                right-=1
        #RETURN THE MAX_AREA
        return max_area
obj=Solution()
height=[1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))