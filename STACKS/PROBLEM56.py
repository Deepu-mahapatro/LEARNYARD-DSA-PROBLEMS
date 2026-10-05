#MERGE INTERVALS 

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # SORT INTERVALS BY STARTING POINT
        intervals.sort()

        # STORE MERGED INTERVALS
        answer = []

        # CHECK EACH INTERVAL
        for start, end in intervals:
            # IF ANSWER IS EMPTY OR THERE IS NO OVERLAP
            if not answer or start > answer[-1][1]:
                # ADD A NEW INTERVAL
                answer.append([start, end])
            else:
                # INTERVALS OVERLAP
                # EXTEND THE END OF THE LAST INTERVAL
                answer[-1][1] = max(answer[-1][1], end)

        # RETURN MERGED INTERVALS
        return answer

# INPUT
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.merge(intervals)

# OUTPUT
print("Merged Intervals:", result)