#BASIC CALCULATOR II 


class Solution:
    def calculate(self, s: str) -> int:
        # STACK STORES NUMBERS AFTER APPLYING THEIR SIGNS
        stack = []

        # CURRENT NUMBER BEING BUILT
        num = 0

        # PREVIOUS OPERATOR
        operator = "+"

        # TRAVERSE THROUGH EACH CHARACTER
        for i, ch in enumerate(s):
            # BUILD MULTI-DIGIT NUMBERS
            if ch.isdigit():
                num = num * 10 + int(ch)

            # PROCESS WHEN AN OPERATOR OR END OF STRING IS REACHED
            if ch in "+-*/" or i == len(s) - 1:
                # ADD NUMBER DIRECTLY FOR ADDITION
                if operator == "+":
                    stack.append(num)

                # STORE NEGATIVE NUMBER FOR SUBTRACTION
                elif operator == "-":
                    stack.append(-num)

                # MULTIPLY WITH THE PREVIOUS NUMBER
                elif operator == "*":
                    stack.append(stack.pop() * num)

                # DIVIDE AND TRUNCATE TOWARD ZERO
                elif operator == "/":
                    previous = stack.pop()
                    result = abs(previous) // abs(num)

                    # RESTORE THE CORRECT SIGN
                    if (previous < 0) != (num < 0):
                        result = -result

                    stack.append(result)

                # RESET NUMBER FOR THE NEXT OPERAND
                num = 0

                # SAVE THE CURRENT OPERATOR
                operator = ch

        # SUM ALL VALUES IN THE STACK
        return sum(stack)


# INPUT
s = "3+2*2"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.calculate(s)

# OUTPUT
print("Result:", result)
