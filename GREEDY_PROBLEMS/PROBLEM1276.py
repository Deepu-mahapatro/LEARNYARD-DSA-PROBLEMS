#NUMBER OF BURGERS WITH NO WASTE OF INGREDIENTS


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):

        # Step 1: Check if tomato slices are odd
        # Every burger requires an even number of tomato slices
        if tomatoSlices % 2 != 0:
            return []

        # Step 2: Calculate the number of Jumbo Burgers
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2

        # Step 3: Calculate the number of Small Burgers
        small = cheeseSlices - jumbo

        # Step 4: Validate burger counts
        # Both counts must be non-negative
        if jumbo < 0 or small < 0:
            return []

        # Step 5: Return [Jumbo Burgers, Small Burgers]
        return [jumbo, small]


# Test cases
obj = Solution()

print(obj.numOfBurgers(16, 7))  # [1, 6]
print(obj.numOfBurgers(17, 4))  # []
print(obj.numOfBurgers(4, 17))  # []
print(obj.numOfBurgers(0, 0))   # [0, 0]
