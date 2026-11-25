#MINIMUM NUMBER OF ARROWS TO BURST BALLOONS


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        # Step 1: Sort balloons by their ending position
        points.sort(key=lambda x: x[1])

        # Step 2: Initialize the arrow count
        arrows = 1

        # Step 3: Store the ending position of the first balloon
        last_end = points[0][1]

        # Step 4: Traverse all balloon intervals
        for start, end in points:

            # Step 5: Check if a new arrow is required
            if start > last_end:

                # Increase arrow count
                arrows += 1

                # Update the arrow position
                last_end = end

        # Step 6: Return minimum arrows required
        return arrows


# Test cases
obj = Solution()

print(obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
# Output: 2

print(obj.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
# Output: 4

print(obj.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
# Output: 2
