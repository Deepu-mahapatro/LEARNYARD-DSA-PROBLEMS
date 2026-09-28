#LONGEST VALID PARENTHESIS 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #STACK STORES THE INDEXES '
        #-1 ACTS AS THE INTIAL BOUNDARY 
        stack=[-1]
        #STORES THE LONGEST VALID PARENTHESES LENGTH
        max_length=0
        #TRAVERSE THE STRING USING INDIXES 
        for i in range(len(s)):
            #IF WE FIND AN OPENING BRACKET 
            if s[i]=='(':
                #STORE ITS INDEX IN THE STACK
                stack.append(i)
            else:
                #IF WE FIND A CLOSING BRACKET,
                #REMOVE THE MATCHING OPEINING BRACKET 
                stack.pop()
                #IF THE STACK BECOMES EMPTY AND CLOSING BRACKET COMES FIRST
                #CURRENT INDEX BECOMES THE NEW BOUNDARY 
                if not stack:
                    stack.append(i)
                else:
                    #CALCULATE THE LENGTH OF THE CURRENT VALID PARENTHESES SUBSTRING
                    length=i-stack[-1]
                    #UPDATE THE MAXIMUM LENGTH 
                    max_length=max(max_length,length)
        #RETURN THE LONGEST VALID PARENTHESES LENGTH 
        return max_length 
s = "((()()))"

solution = Solution()
result = solution.longestValidParentheses(s)

print(result)