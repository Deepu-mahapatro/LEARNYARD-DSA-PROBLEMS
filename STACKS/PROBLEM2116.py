#CHECK IS A PARENTHESIS STRING CAN BE VALID OR NOT 

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #A VALID PARENTHESIS STRING MUST HAVE EVEN LENGTH 
        if len(s)%2==1:
            return False
        #LOW=MINIMUM POSSIBLE BALANCE 
        #HIGH=MAXIMUM POSSIBLE BALANCE 
        low=0
        high=0
        #TRAVERSE EVERY CHARACTER
        for i in range(len(s)):
            #IF THE CHARACTER IS UNLOCKED 
            #WE CAN CHOOSE IT AS "(" OR ")"
            if locked[i]=="0":
                #CHOOSING ")" GIVES THE MINIMUM BALANCE 
                low-=1
                #CHOOSING "(" GIVES THE MAXIMUM BALANCE 
                high+=1
            #IF THE CHARACTER IS LOCKED 
            else:
                #IF IT IS "("
                if s[i]=="(":
                    #BOTH MINIMUM AND MAXIMUM BALANCE INCREASE 
                    low+=1
                    high+=1
                #IF IT IS ")"
                else:
                    #BOTH MINIMUM AND MAXIMUM BALANCE DECREASE 
                    low-=1
                    high-=1
            #A VALID PARENTHESIS STRING CAN NEVER 
            #HAVE A NEGATIVE BALANCE
            low=max(low,0)
            #IF EVEN THE MAXIMUM POSSIBLE BALANCE 
            #BECOMES NEGATIVE, IT IS IMPOSSIBLE 
            if high<0:
                return False 
        #LOW==0 MEANS WE CAN MAKE THE FINAL BALANCE ZERO 
        return low==0
solution = Solution()

s = "))()))"
locked = "010100"

result = solution.canBeValid(s, locked)

print("Input:", s)
print("Locked:", locked)
print("Can Be Valid:", result)