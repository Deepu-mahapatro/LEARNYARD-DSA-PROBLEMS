#MINIMUM SECONDS TO EQUALIZE A CIRCULAR ARRAY 


class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:

        # Step 1: Get the length of the array
        n = len(nums)

        # Step 2: Initialize a Hash Map
        # Store each value and its occurrence indices
        positions = {}

        # Step 3: Traverse the array and store indices
        for i in range(n):

            # If the value is not present, initialize an empty list
            if nums[i] not in positions:
                positions[nums[i]] = []

            # Store the current index of the value
            positions[nums[i]].append(i)

        # Step 4: Initialize minimum seconds
        min_seconds = float('inf')

        # Step 5: Traverse the Hash Map
        for value, indices in positions.items():

            # Initialize maximum gap for the current value
            max_gap = 0

            # Step 6: Calculate gaps between consecutive occurrences
            for i in range(len(indices) - 1):

                # Difference between consecutive indices
                gap = indices[i + 1] - indices[i]

                # Update the maximum gap
                max_gap = max(max_gap, gap)

            # Step 7: Calculate the circular gap
            # Distance from the last occurrence back to the first
            circular_gap = n - indices[-1] + indices[0]

            # Include the circular gap in the maximum gap
            max_gap = max(max_gap, circular_gap)

            # Step 8: Calculate seconds required for this value
            seconds = max_gap // 2

            # Step 9: Update minimum seconds
            min_seconds = min(min_seconds, seconds)

        # Step 10: Return the minimum seconds
        return min_seconds


# ---------------------------------
# Test cases
# ---------------------------------

obj = Solution()

print(obj.minimumSeconds([1, 2, 1, 2, 1]))
# Output: 1

print(obj.minimumSeconds([2, 1, 3, 3, 2]))
# Output: 2

print(obj.minimumSeconds([5, 5, 5, 5]))
# Output: 0

print(obj.minimumSeconds([1, 2, 3, 4]))
# Output: 2
