#REMOVE DUPLICATE LETTERS 


from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # Step 1: Count the frequency of each character
        freq = Counter(s)

        # Step 2: Initialize an empty stack and a set
        stack = []       # Stores characters for the final result
        seen = set()     # Tracks characters already in the stack

        # Step 3: Traverse the string
        for ch in s:

            # Decrease the remaining frequency of current character
            freq[ch] -= 1

            # If character is already present, skip it
            if ch in seen:
                continue

            # Step 4: Greedy condition
            # Remove larger characters if they appear again later
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:

                removed = stack.pop()

                # Allow the removed character to be added again later
                seen.remove(removed)

            # Step 5: Add current character to stack and set
            stack.append(ch)
            seen.add(ch)

        # Step 6: Convert stack into a string and return
        return "".join(stack)


# Test cases
obj = Solution()

print(obj.removeDuplicateLetters("bcabc"))