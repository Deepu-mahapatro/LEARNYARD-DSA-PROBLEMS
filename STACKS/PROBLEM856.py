#SCORE OF THE PARENTHESIS

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        # THE STACK STORES THE SCORES OF EACH CURRENTLY
        # OPEN PARENTHESIS LEVEL.
        #
        # WE START WITH 0 BECAUSE THE OUTERMOST LEVEL
        # HAS NO SCORE YET.
        stack = [0]

        # TRAVERSE THE STRING FROM LEFT TO RIGHT.
        for ch in s:

            # IF WE SEE AN OPENING PARENTHESIS '(',
            # WE CREATE A NEW LEVEL WITH SCORE 0.
            if ch == '(':
                stack.append(0)

            # IF WE SEE A CLOSING PARENTHESIS ')',
            # WE NEED TO CALCULATE THE SCORE OF THIS LEVEL.
            else:

                # REMOVE THE SCORE BELONGING TO THE
                # CURRENT PARENTHESIS LEVEL.
                current_score = stack.pop()

                # IF CURRENT_SCORE IS 0,
                # IT MEANS WE FOUND AN EMPTY PAIR "()".
                #
                # ACCORDING TO THE RULE:
                # () = 1
                if current_score == 0:
                    current_score = 1

                # OTHERWISE, WE HAVE SOMETHING LIKE "(A)".
                #
                # ACCORDING TO THE RULE:
                # (A) = 2 * A
                else:
                    current_score = 2 * current_score

                # ADD THE CALCULATED SCORE TO THE
                # PREVIOUS PARENTHESIS LEVEL.
                stack[-1] += current_score

        # RETURN THE FINAL SCORE STORED AT THE
        # BOTTOM OF THE STACK.
        return stack[0]


# TAKE INPUT FROM THE USER.
s = input("Enter the parentheses string: ")

# CREATE AN OBJECT OF THE SOLUTION CLASS.
obj = Solution()

# CALL THE FUNCTION AND STORE THE ANSWER.
result = obj.scoreOfParentheses(s)

# PRINT THE FINAL SCORE.
print("Score:", result)