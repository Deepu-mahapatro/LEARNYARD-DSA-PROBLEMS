#CANDY 


class Solution:
    def candy(self, ratings: list[int]) -> int:

        n = len(ratings)

        # Step 1: Give every child at least 1 candy
        candies = [1] * n

        # Step 2: Left-to-right traversal
        # If current rating is greater than the left neighbor,
        # current child must receive more candies.
        for i in range(1, n):

            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right-to-left traversal
        # If current rating is greater than the right neighbor,
        # current child must receive more candies.
        for i in range(n - 2, -1, -1):

            if ratings[i] > ratings[i + 1]:

                # Take the maximum to preserve the left-side condition
                candies[i] = max(
                    candies[i],
                    candies[i + 1] + 1
                )

        # Step 4: Return the minimum total candies
        return sum(candies)


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.candy([1, 0, 2]))
# Output: 5

print(obj.candy([1, 2, 2]))
# Output: 4

print(obj.candy([1, 3, 4, 5, 2]))
# Output: 11

print(obj.candy([1, 2, 3, 4, 5]))
# Output: 15
