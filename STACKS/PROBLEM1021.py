#REMOVE OUTER MOST PARENTHESIS

class Solution:

    def removeOuterParentheses(self, s: str) -> str:

        # Depth tells us how many '(' brackets
        # we are currently inside
        depth = 0

        # Store the final answer
        result = []

        # Go through every character
        for ch in s:

            # If we see an opening bracket
            if ch == "(":

                # If depth is 0, we are currently
                # outside any parentheses.
                # Therefore, this '(' is outermost.
                if depth > 0:
                    result.append(ch)

                # Enter one level deeper
                depth += 1

            # If we see a closing bracket
            else:

                # Leave the current level
                depth -= 1

                # If depth is still greater than 0,
                # this ')' is NOT the outermost one.
                if depth > 0:
                    result.append(ch)

        # Convert the list into a string
        return "".join(result)
solution = Solution()

s = "(()())(())"

result = solution.removeOuterParentheses(s)

print("Input:", s)
print("Output:", result)