#MINIMUM DIFFERNCE BETWEEN HIGJEST AND LOWEST OF K SCORES 


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        # Step 1: Sort the array in ascending order
        nums.sort()

        # Step 2: Initialize the minimum difference
        min_diff = float('inf')

        # Step 3: Traverse the array using a sliding window
        # Each window contains exactly k elements
        for i in range(len(nums) - k + 1):

            # Step 4: Calculate the difference between
            # the highest and lowest scores in the window
            diff = nums[i + k - 1] - nums[i]

            # Step 5: Update the minimum difference
            min_diff = min(min_diff, diff)

        # Step 6: Return the minimum difference
        return min_diff


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.minimumDifference([90, 1, 55, 30, 10], 3))
# Output: 29

print(obj.minimumDifference([9, 4, 1, 7], 2))
# Output: 2

print(obj.minimumDifference([1], 1))
# Output: 0
