#MINIMUM NUMBER OF OPERATIONS TO MAKE WORD K-PERIODIC

from typing import List
from collections import Counter
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        #STORE ALL TEH SUBSTRINGS OF LENGTH K
        substrings=[]
        #DIVIDE THE WORD INTO NON-OVERLAPPING SUBSTRINGS
        for i in range(0,len(word),k):
            substrings.append(word[i:i+k])
        #COUNT HOW MANY TIMES EACH SUBSTRING APPEARS
        frequency=Counter(substrings)
        #FIND THE HIGHEST FREQUENCY 
        #THIS IS THE SUBSTRING WE WILL KEEP
        maximum_frequency=max(frequency.values())
        #FIND TOTAL NUMBER OF SUBSTRINGS 
        total_substrings=len(substrings)
        #MINIMUM OPERATIONS=TOTAL SUBSTRINGS - MOST FREQUENCY SUBSTRING COUNT
        return total_substrings-maximum_frequency
obj=Solution()
word="bcaabccababc"
k=3
print(obj.minimumOperationsToMakeKPeriodic(word,k))