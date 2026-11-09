#SMALLEST STRING AFTER SUBSTRING OPERATION


class Solution:
    def smallestString(self, s: str) -> str:

        # Convert string into a list because strings are immutable
        chars = list(s)
        n = len(chars)

        # Step 1: Skip all leading 'a' characters
        i = 0

        while i < n and chars[i] == 'a':
            i += 1

        # Step 2: If all characters are 'a',
        # change only the last character to 'z'
        if i == n:
            chars[-1] = 'z'
            return "".join(chars)

        # Step 3: Decrement characters until we reach
        # another 'a' or the end of the string
        while i < n and chars[i] != 'a':
            chars[i] = chr(ord(chars[i]) - 1)
            i += 1

        # Step 4: Convert the list back into a string
        return "".join(chars)


# Testing
obj = Solution()

print(obj.smallestString("acbbc"))  # abaab
print(obj.smallestString("cbabc"))  # baabc
print(obj.smallestString("aaa"))    # aaz
print(obj.smallestString("leetcode"))  # kddsbncd
