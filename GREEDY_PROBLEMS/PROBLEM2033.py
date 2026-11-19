#MINIMUM OPERATIONS TO MAKE A UNI-VALID GRID 


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:

        # Step 1: Flatten the 2D grid into a 1D array
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)

        # Step 2: Get the total number of elements
        n = len(nums)

        # Step 3: Get the remainder of the first element
        remainder = nums[0] % x

        # Step 4: Check whether all elements have the same remainder
        # If remainders differ, making all elements equal is impossible
        for num in nums:
            if num % x != remainder:
                return -1

        # Step 5: Sort the array in ascending order
        nums.sort()

        # Step 6: Find the median element
        # The median is the optimal target for minimizing operations
        median = nums[n // 2]

        # Step 7: Initialize the operation counter
        operations = 0

        # Step 8: Calculate the operations required for each element
        for num in nums:

            # Find the absolute difference between the element and median
            difference = abs(num - median)

            # Each operation changes the element by exactly x
            operations += difference // x

        # Step 9: Return the minimum number of operations
        return operations


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.minOperations([[2, 4], [6, 8]], 2))
# Output: 4

print(obj.minOperations([[1, 5], [2, 3]], 1))
# Output: 5

print(obj.minOperations([[1, 2], [3, 4]], 2))
# Output: -1
