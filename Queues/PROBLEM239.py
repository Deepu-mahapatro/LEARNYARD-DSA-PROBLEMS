#SLIDING WINDOW MAXIMUM 

from collections import deque 
class Solution:
    def maxSlidingWindow(self,nums,k):
        #WE CREATE A DEQUE WHICH STORES THE INDEXES OF TEH DEQUE
        dq=deque()
        #STORE MAXIMUM VALUES OF EACH WINDOW 
        result=[]
        #GO THROUGH THE ARRAY FROM LEFT TO RIGHT 
        for i in range(len(nums)):
            #REMOVE THE INDEX FORM THE FRONT OF IT IS OUTSIDE THE CURRENT WINDOW 
            if dq and dq[0]<=i-k:
                dq.popleft()
                #REMOVE ALL SMALLER OR EQUAL ELEMENTS FORM HE BACK OF THE DEQUE 
                #THEY CANNOT BECOME THE MAXIMUM WHILE THE CURRENT ELEMENTS IS IN THE WINDOW 
                while dq and nums[dq[-1]]<=nums[i]: 
                    dq.pop()
                #ADD THE CURRENT INDEX TO THE DEQUE
                dq.append(i)
                #WHEN WE HAVE A COMPLETE WINDOW THE FRONT DEQUE HAS THE MAXIMUM VALUE 
                if i>=k-1:
                    result.append(nums[dq[0]])
        #RETURN THE MAXIMUM VALUE OF ECAH WINDOW 
        return result 
obj = Solution()

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

result = obj.maxSlidingWindow(nums, k)

print("Input:", nums)
print("K:", k)
print("Maximum of Each Window:", result)