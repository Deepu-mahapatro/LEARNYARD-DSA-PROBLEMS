#REPLACE NON-COPRIME NUMBERS IN AN ARRAY 

import math
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        # STACK STORES THE FINAL NUMBERS
        stack = []
        # TRAVERSE THROUGH EACH NUMBER
        for num in nums:
            # CURRENT NUMBER MAY NEED TO BE MERGED
            current = num
            # CHECK WITH THE TOP OF THE STACK
            while stack:
                # FIND GCD OF TOP NUMBER AND CURRENT NUMBER
                gcd = math.gcd(stack[-1], current)
                # IF GCD IS 1, THEY ARE COPRIME
                if gcd == 1:
                    break
                # REMOVE THE TOP NUMBER
                previous = stack.pop()
                # CALCULATE LCM
                current = (previous // gcd) * current
            # PUSH FINAL NUMBER INTO STACK
            stack.append(current)
        # RETURN FINAL ARRAY
        return stack

# INPUT
nums = [6, 4, 3, 2, 7, 6, 2]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.replaceNonCoprimes(nums)

# OUTPUT
print("Final Array:", result)
