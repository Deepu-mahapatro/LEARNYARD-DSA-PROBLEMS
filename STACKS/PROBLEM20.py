#VALID PARENTHESIS

class Solution:
    def isValid(self,s:str) -> bool:
        #STACK TO STORE OPENING BRACKETS 
        stack=[]
        #CLOSING BRACKET -> MATCHING OPENING BRACKET
        pairs={
            ']':'[',
            '}':'{',
            ')':'('
        }
        #TRAVERSE THE STRING 
        for i in s:
            #IF OPENING BRACKET, PUSH IT INTO THE STACK 
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            #IF CLOSING BRACKET 
            else:
                #NO OPENING BRACKET AVAILABLE 
                if not stack:
                    return False
                #CHECK WHETHER TEH TOP MATCHES 
                if stack[-1]!=pairs[i]:
                    return False
                #REMOVE THE MATCHED OPENING BRACKET
                stack.pop()
        #STACK SHOULD BE EMPTY AFTER ALL MATCHES 
        return len(stack)==0
s="{[]}"
solution=Solution()
result=solution.isValid(s)
print(result)