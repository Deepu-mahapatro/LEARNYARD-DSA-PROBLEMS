#COUNT PAIRS THAT FORM A COMPLETE DAY II

from typing import List
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        #DIXTIONARY TO STORE HOW MANY TIMES EACH REMAINDER (0 TO 23) HAS APPEARED
        remainder_count={}
        #VARIABLE TO STORE THE ANSWER 
        pairs=0
        #TRAVERSE EVERY HOUR 
        for hour in hours:
            #FIND REMAINDER WHEN DIVIDED BY 24
            remainder=hour%24
            #FIND THE REQUIRED REMAINDER
            needed=(24-remainder)%24
            #IF SUCH REMAINDER HAS ALREADY APPEARED
            #THEN EACH OCCURENCE FORMS A VALID PAIR 
            if needed in remainder_count:
                pairs+=remainder_count[needed]
            #STORE THE CURRENT REMAINDER
            remainder_count[remainder]=remainder_count.get(remainder,0)+1
        #RETURN TOTAL PAIRS
        return pairs
obj=Solution()
hours=[8,16,5,19]
print(obj.countCompleteDayPairs(hours))