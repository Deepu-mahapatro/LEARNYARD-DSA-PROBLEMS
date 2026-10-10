#BASIC CALCULATOR 


class Solution:
    def calculate(self, s: str) -> int:
        # STACK STORES PREVIOUS RESULTS AND SIGNS
        stack = []

        # CURRENT NUMBER BEING BUILT
        num = 0

        # CURRENT SIGN: 1 FOR PLUS, -1 FOR MINUS
        sign = 1

        # CURRENT RUNNING RESULT
        result = 0

        # TRAVERSE EACH CHARACTER IN THE STRING
        for ch in s:
            # BUILD MULTI-DIGIT NUMBERS
            if ch.isdigit():
                num = num * 10 + int(ch)

            # PROCESS ADDITION OR SUBTRACTION
            elif ch in "+-":
                # ADD THE PREVIOUS NUMBER WITH ITS SIGN
                result += sign * num

                # RESET NUMBER FOR THE NEXT OPERAND
                num = 0

                # UPDATE SIGN FOR THE NEXT NUMBER
                sign = 1 if ch == "+" else -1

            # SAVE CURRENT CONTEXT BEFORE ENTERING PARENTHESES
            elif ch == "(":
                stack.append(result)
                stack.append(sign)

                # START A NEW EXPRESSION INSIDE PARENTHESES
                result = 0
                sign = 1

            # FINISH THE EXPRESSION INSIDE PARENTHESES
            elif ch == ")":
                # ADD THE LAST NUMBER INSIDE PARENTHESES
                result += sign * num
                num = 0

                # APPLY THE SIGN BEFORE THE PARENTHESES
                result *= stack.pop()

                # ADD THE RESULT FROM BEFORE THE PARENTHESES
                result += stack.pop()

        # ADD THE FINAL NUMBER
        result += sign * num

        # RETURN THE FINAL ANSWER
        return result


# INPUT
s = "(1+(4+5+2)-3)+(6+8)"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.calculate(s)

# OUTPUT
print("Result:", result)
