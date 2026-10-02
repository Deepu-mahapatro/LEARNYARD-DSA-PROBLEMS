#MINIMUM INSERTIONS TO BALANCE A PARENTHESIS STRING 

class Solution:
    def minInsertions(self, s: str) -> int:
        #BALANCE REPRESENTS HOW MANY ")" WE CURRENTLY NEED
        balance=0
        #STORES TEH NUMBER OF PARENTHESIS WE NEED TO INSERT 
        insertions=0
        #TRAVERSE EVERY CHARACTER
        for ch in s:
            #IF WE FOUND "(" IT NEEDS TWO ")" TO BALANCE IT 
            if ch=="(":
                #IF BALANCE IS ODD, ONE ")" IS STILL NEEDED 
                #TO COMPLETE THE PREVIOUS ")" PAIR 
                if balance%2==1:
                    insertions+=1
                    balance-=1
                balance+=2
            #IF WE FOUND ")"
            else:
                #ONE REQUIRED ")" HAS BEEN FOUND 
                balance-=1
                #IF THE BALANCE BECOMES -1
                #WE HAVE EXTRA ")" WITH NO "(" BEFORE IT 
                if balance==-1:
                    #INSERT ONE "(" BEFORE THIS ")"
                    insertions+=1
                    #THE INSERTED "(" NEEDS TWO ")"
                    #THE CURRENT ")" SATISFIES ONE OF THEM 
                    #SO ONLY ONE ")" IS STILL NEEDED 
                    balance=1
        #IF BALANCE IS STILL GREATER THEN 0
        #THESES MANY ")" STILL MISSING 
        insertions+=balance
        #RETURN THE MINIMUM NUMBER OF INSERTIONS 
        return insertions
solution = Solution()

s = "(()))(()))()())))"

result = solution.minInsertions(s)

print("Input:", s)
print("Minimum Insertions:", result)