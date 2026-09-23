#DOTA 2 SENATE

from collections import deque
class Solution:
    def predictPartyVictory(self,senate):
        #LENGTH IF THE SENATE STRING 
        n=len(senate)
        #CREATE TWO QUEUES 
        #RADIANT STORES THE INDEXES OF 'R' SENATORS 
        #DIRE STORES TEH INDEXES OF 'D' SENATORS 
        radiant=deque()
        dire=deque()
        #GO THROUGH TEH SENATE STRING AND STORE  THE INDEXES IN THEIR RESPECTIVE QUEUES 
        for i in range(n):
            if senate[i]=="R":
                radiant.append(i)
            else:
                dire.append(i)
        #CONTINUE UNTIL ONE PARTY HAS NO SENATORS LEFT 
        while radiant and dire:
            #GET THE NEXT RADIANT SENATOR 
            r=radiant.popleft()
            #GET THE NEXT DIRE SENATOR 
            d=dire.popleft()
            #IF RADIANT SENATOR APPEARS FIRST THEN BANS THE DIRE SENATOR 
            if r<d:
                #RADIANT SURVIVES AND GETS ANOTHER TURN IN THE NEXT ROUNFD 
                radiant.append(r+n)
            else:
                #DIRE SENATOR APPEARS FIRST THEN DIRE BANS THE RADIANT SENATOR 
                #DIRE SURVIVES AND GETS ANOTHER TURN IN  THE NEXT ROUND 
                dire.append(d+n)
        #IF RADIANT QUEUE STILL HAS SENATORS THEN RADIANT WINS 
        if radiant:
            return "Radiant"
        else:
            #OTHERWISE THE DIRE SENATOR WINS 
            return "Dire"
obj = Solution()

senate = "RDD"

result = obj.predictPartyVictory(senate)

print("Senate:", senate)
print("Winner:", result)