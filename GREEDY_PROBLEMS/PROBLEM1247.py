#MINIMUM SWAPS TO MAKE STRING EQUAL


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        # Count the two types of mismatches
        xy = 0
        yx = 0

        # Traverse both strings simultaneously
        for i in range(len(s1)):

            # If characters are equal, no action is needed
            if s1[i] == s2[i]:
                continue

            # Count x-y mismatches
            elif s1[i] == 'x' and s2[i] == 'y':
                xy += 1

            # Count y-x mismatches
            else:
                yx += 1

        # If total mismatches are odd, making strings equal is impossible
        if (xy + yx) % 2 != 0:
            return -1

        # Each pair of same-type mismatches requires one swap
        swaps = (xy // 2) + (yx // 2)

        # One remaining xy and one remaining yx require two swaps
        if xy % 2 == 1:
            swaps += 2

        return swaps


# Driver code for VS Code
s1 = "xx"
s2 = "yy"

obj = Solution()
result = obj.minimumSwap(s1, s2)

print("Minimum swaps required:", result)
