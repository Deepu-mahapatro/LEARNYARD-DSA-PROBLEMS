#FIND TEH WINNER IF THE CIRCULAR GAME 

from collections import deque 
class Solution:
    def findTheWinner(self,n,k):
        #CREATE A QUEUE STORE ALL THE FRIENDS FROM 1 TO N
        friends=deque(range(1,n+1))
        #CONTINUE UNTIL ONLY ONE FRIEND IS LEFT 
        while len(friends)>1:
            #MOVE K-1 FRIENDS FROM THE FRONT TO THE BACK 
            #WE DO K-1 BECAUSE THE K-TH FRIEND IS THE ONE WE NEED TO ELIMINATE 
            for _ in range(k-1):
                #REMOVE THE FRIEND FROM THE FRONT AND ADD THEM TO THE BACK 
                friends.append(friends.popleft())
            #REMOVE THE K-TH FRIEND (THIS FRIEND IS ELIMINATED)
            friends.popleft()
        #ONLY ONE FRIEND IS LEFT THAT FRIEND IS THE WINNER 
        return friends[0]
obj = Solution()

n = 5
k = 2

result = obj.findTheWinner(n, k)

print("Number of Friends:", n)
print("K:", k)
print("Winner:", result)