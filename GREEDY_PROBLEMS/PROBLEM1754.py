#LARGEST MERGE OF TWO STRINGS


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        # Step 1: Initialize two pointers
        i = 0
        j = 0

        # Store the merged characters
        result = []

        # Step 2: Traverse both strings
        while i < len(word1) and j < len(word2):

            # Step 3: Compare the remaining suffixes
            if word1[i:] > word2[j:]:

                # Choose character from word1
                result.append(word1[i])
                i += 1

            else:
                # Choose character from word2
                result.append(word2[j])
                j += 1

        # Step 4: Append remaining characters from word1
        result.extend(word1[i:])

        # Step 5: Append remaining characters from word2
        result.extend(word2[j:])

        # Step 6: Convert list into string
        return "".join(result)


# Test cases
obj = Solution()

print(obj.largestMerge("cabaa", "bcaaa"))
print(obj.largestMerge("abcabc", "abdcaba"))
