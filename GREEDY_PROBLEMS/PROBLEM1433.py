#FREQUENCY COUNTING APPROACH


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        # Step 1: Create frequency arrays for 26 lowercase letters
        freq1 = [0] * 26
        freq2 = [0] * 26

        # Step 2: Count the frequency of characters in s1
        for ch in s1:
            index = ord(ch) - ord('a')
            freq1[index] += 1

        # Step 3: Count the frequency of characters in s2
        for ch in s2:
            index = ord(ch) - ord('a')
            freq2[index] += 1

        # Step 4: Assume both breaking conditions are possible
        check1 = True
        check2 = True

        # Step 5: Initialize cumulative frequency differences
        count1 = 0
        count2 = 0

        # Step 6: Compare cumulative frequencies alphabetically
        for i in range(26):

            count1 += freq1[i] - freq2[i]
            count2 += freq2[i] - freq1[i]

            # If count1 becomes negative, this direction fails
            if count1 < 0:
                check1 = False

            # If count2 becomes negative, the opposite direction fails
            if count2 < 0:
                check2 = False

        # Step 7: Return True if either direction is possible
        return check1 or check2


# Test the solution
obj = Solution()

s1 = "abc"
s2 = "xya"

result = obj.checkIfCanBreak(s1, s2)

print("Can one string break the other?", result)
