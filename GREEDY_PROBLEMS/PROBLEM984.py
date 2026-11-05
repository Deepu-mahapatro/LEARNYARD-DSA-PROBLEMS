#STRING WITHOUT AAA OR BBB


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        # Step 1: Initialize the result list
        result = []

        # Step 2: Find maximum and minimum frequencies
        max_freq = max(a, b)
        min_freq = min(a, b)

        # Step 3: Check whether a valid string is possible
        if max_freq > 2 * (min_freq + 1):
            return ""

        # Step 4: Construct the string using Greedy
        while a > 0 or b > 0:

            # Check whether the last two characters are identical
            if len(result) >= 2 and result[-1] == result[-2]:

                # If the last two characters are 'aa', append 'b'
                if result[-1] == 'a':
                    result.append('b')
                    b -= 1

                # If the last two characters are 'bb', append 'a'
                else:
                    result.append('a')
                    a -= 1

            # Otherwise, select the character with higher frequency
            elif a >= b and a > 0:
                result.append('a')
                a -= 1

            else:
                result.append('b')
                b -= 1

        # Step 5: Convert the result list into a string
        return "".join(result)


# Create an object
obj = Solution()

# Test Case 1
print(obj.strWithout3a3b(1, 2))

# Test Case 2
print(obj.strWithout3a3b(4, 1))

# Test Case 3
print(obj.strWithout3a3b(1, 3))

# Test Case 4
print(obj.strWithout3a3b(5, 2))
