#REVERSE SUBARRAY TO MAXIMIZE ARRAY VALUE 


class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:

        # Step 1: Initialize variables
        n = len(nums)

        total_sum = 0
        max_gain = 0

        max_left = float('-inf')
        min_right = float('inf')

        # Step 2: Traverse adjacent elements
        for i in range(n - 1):

            # Calculate original array value
            diff = abs(nums[i] - nums[i + 1])
            total_sum += diff

            # Case 1: Reverse a subarray touching boundaries
            gain1 = abs(nums[0] - nums[i + 1]) - diff

            gain2 = abs(nums[n - 1] - nums[i]) - diff

            max_gain = max(max_gain, gain1, gain2)

            # Case 2: Find maximum minimum and minimum maximum
            max_left = max(
                max_left,
                min(nums[i], nums[i + 1])
            )

            min_right = min(
                min_right,
                max(nums[i], nums[i + 1])
            )

        # Step 3: Calculate internal reversal gain
        max_gain = max(
            max_gain,
            2 * (max_left - min_right)
        )

        # Step 4: Return maximum possible array value
        return total_sum + max_gain


# Test case
obj = Solution()

nums = [2, 3, 1, 5, 4]

print(obj.maxValueAfterReverse(nums))
# Output: 10
