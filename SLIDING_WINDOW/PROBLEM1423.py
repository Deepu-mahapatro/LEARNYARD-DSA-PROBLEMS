#MAXIMUM POINTS YOU CAN OBTAIN FROM CARDS

from typing import List
class Solution:
    def maxScore(self,cardPoints,k):
        n=len(cardPoints)
        #TOTAL SUM OF ALL CARDS
        total_sum=sum(cardPoints)
        #SIZE OF THE REMAINING WINDOW
        window_size=n-k
        #IF TAKING ALL CARDS
        if window_size==0:
            return total_sum
        #FIRST WINDOW SUM
        window_sum=sum(cardPoints[:window_size])
        min_window_sum=window_sum
        #SLIDE THE WINDOW
        for i in range(window_size,n):
            window_sum=window_sum-cardPoints[i-window_size]+cardPoints[i]
            min_window_sum=min(min_window_sum,window_sum)
        #RETURN MAXIMUM SCORE
        return total_sum-min_window_sum
obj=Solution()
cardPoints=[1,2,3,4,5,6,1]
k=3
print(obj.maxScore(cardPoints,k))
