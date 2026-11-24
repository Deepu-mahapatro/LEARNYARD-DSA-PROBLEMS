#NON-OVERLAPPING INTERVALS

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        # Step 1: Get the total number of intervals
        n = len(intervals)

        # Step 2: Sort intervals based on ending time
        intervals.sort(key=lambda x: x[1])

        # Step 3: Initialize variables
        count = 0
        prev_end = float('-inf')

        # Step 4: Traverse all intervals
        for i in range(n):

            # Step 5: Check whether the current interval overlaps
            if intervals[i][0] < prev_end:

                # Remove the overlapping interval
                count += 1

            else:

                # Update the previous ending time
                prev_end = intervals[i][1]

        # Step 6: Return the minimum number of removals
        return count


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
# Output: 1

print(obj.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
# Output: 2

print(obj.eraseOverlapIntervals([[1, 2], [2, 3]]))
# Output: 0
