#CONSTRUCT SMALLEST NUMBER DI STRING 

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # STACK STORES NUMBERS TEMPORARILY
        stack = []
        # STORES THE FINAL ANSWER
        answer = ""
        # START GENERATING NUMBERS FROM 1
        num = 1
        # TRAVEL THROUGH THE PATTERN
        for ch in pattern:
            # PUSH CURRENT NUMBER INTO STACK
            stack.append(num)
            # MOVE TO NEXT NUMBER
            num += 1
            # WHEN WE SEE I
            # EMPTY THE STACK
            if ch == "I":
                while stack:
                    # POP IN REVERSE ORDER
                    # AND ADD TO ANSWER
                    answer += str(stack.pop())
        # ADD THE LAST NUMBER
        # PATTERN HAS ONE MORE NUMBER THAN CHARACTERS
        stack.append(num)
        # EMPTY REMAINING STACK
        while stack:
            # POP IN REVERSE ORDER
            answer += str(stack.pop())
        # RETURN SMALLEST NUMBER
        return answer

# INPUT
pattern = "IDID"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.smallestNumber(pattern)

# OUTPUT
print("Smallest Number:", result)