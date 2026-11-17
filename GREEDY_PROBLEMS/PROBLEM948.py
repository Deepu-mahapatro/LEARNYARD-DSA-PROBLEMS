#BAG OF TOKENS


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:

        # Step 1: Sort tokens in ascending order
        tokens.sort()

        # Step 2: Initialize two pointers
        left = 0                       # Smallest token
        right = len(tokens) - 1       # Largest token

        # Step 3: Initialize score variables
        score = 0
        max_score = 0

        # Step 4: Traverse using two pointers
        while left <= right:

            # Step 5: Check whether we can play
            # the smallest token face-up
            if power >= tokens[left]:

                # Spend power to increase score
                power -= tokens[left]
                score += 1

                # Move left pointer forward
                left += 1

                # Update maximum score
                max_score = max(max_score, score)

            # Step 6: If we cannot play face-up,
            # check whether we can play face-down
            elif score > 0:

                # Sacrifice 1 score to gain power
                power += tokens[right]
                score -= 1

                # Move right pointer backward
                right -= 1

            # Step 7: Stop if neither operation is possible
            else:
                break

        # Step 8: Return maximum score achieved
        return max_score


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.bagOfTokensScore([100], 50))
# Output: 0

print(obj.bagOfTokensScore([100, 200], 150))
# Output: 1

print(obj.bagOfTokensScore([100, 200, 300, 400], 200))
# Output: 2

print(obj.bagOfTokensScore([200, 100], 150))
# Output: 1
