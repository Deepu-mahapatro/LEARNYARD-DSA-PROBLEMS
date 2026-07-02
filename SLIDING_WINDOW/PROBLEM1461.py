#CHECK IF A STRING CONTAINS ALL BINARY CODES OF SIZE K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #SET TO STORE UNIQUE BINARY SUBSTRINGS OF LENGTH K
        seen=set()
        #SLIDE THE WINDOW FROM LEFT TO RIGHT
        for i in range(len(s)-k+1):
            #CURRENT WINDOW (SUBSTRING OF LENGTH K)
            window=s[i:i+k]
            #STORE IT IN THE SET
            seen.add(window)
        #TOTAL POSSIBLE BINARY CODES=2^K
        total_codes=2**k
        #IF WE FOUND ALL POSSIBLE CODES,RETURN TRUE
        return len(seen)==total_codes
#INPUT 
s="00110110"
k=2
#CREATE OBJECT
obj=Solution()
#CALL THE FUNCTION
result=obj.hasAllCodes(s,k)
#PRINT THE RESULT
print(result)