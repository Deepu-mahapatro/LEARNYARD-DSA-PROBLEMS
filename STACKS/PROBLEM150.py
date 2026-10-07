#EVALUATE REVERSE POLISH NOTATION 

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # STACK STORES NUMBERS AND INTERMEDIATE RESULTS
        stack = []
        # TRAVERSE THROUGH EACH TOKEN
        for token in tokens:
            # IF TOKEN IS AN OPERATOR
            if token in "+-*/":
                # POP SECOND OPERAND
                b = stack.pop()
                # POP FIRST OPERAND
                a = stack.pop()
                # PERFORM THE OPERATION
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    # TRUNCATE DIVISION TOWARD ZERO
                    result = int(a / b)
                # PUSH RESULT BACK INTO STACK
                stack.append(result)
            else:
                # TOKEN IS A NUMBER, SO PUSH IT INTO STACK
                stack.append(int(token))
        # FINAL VALUE IN STACK IS THE ANSWER
        return stack[-1]
# INPUT
tokens = ["2", "1", "+", "3", "*"]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.evalRPN(tokens)

# OUTPUT
print("Result:", result)