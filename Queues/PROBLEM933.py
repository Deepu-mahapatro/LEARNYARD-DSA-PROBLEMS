#NUMBER OIF RECENT CALLS 

from collections import deque
class RecentCounter:
    def __init__(self):
        #CREATE A QUEUE WE STORE REQUEST TIMES HERE
        self.queue=deque()
    def ping(self,t):
        #ADD THE CURRENT REQUEST TIME 
        self.queue.append(t)
        #REMOVE REQUESTS THAT ARE OLDER THAN t-3000 MILLISECONDS
        #VALID RANGE IS : [t-3000,t]
        while self.queue[0]<t-3000:
            #REMOVE THE OLDEST REQUEST 
            self.queue.popleft()
        #RETURN NUMBER OF REQUESTS PRESENT IN THE LAST 3000 MILLISECONDS 
        return len(self.queue)
obj = RecentCounter()

print("ping(1):", obj.ping(1))
print("ping(100):", obj.ping(100))
print("ping(3001):", obj.ping(3001))
print("ping(3002):", obj.ping(3002))