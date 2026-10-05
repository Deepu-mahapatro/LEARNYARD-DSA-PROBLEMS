#INSERT INTERVALS 

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # STORE FINAL INTERVALS
        answer = []

        # GET START AND END OF NEW INTERVAL
        new_start, new_end = newInterval

        # STARTING INDEX
        i = 0

        # NUMBER OF INTERVALS
        n = len(intervals)

        # ADD INTERVALS COMPLETELY BEFORE NEW INTERVAL
        while i < n and intervals[i][1] < new_start:
            answer.append(intervals[i])
            i += 1

        # MERGE ALL OVERLAPPING INTERVALS
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        # ADD MERGED NEW INTERVAL
        answer.append([new_start, new_end])

        # ADD REMAINING INTERVALS
        while i < n:
            answer.append(intervals[i])
            i += 1

        # RETURN FINAL RESULT
        return answer
# INPUT
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.insert(intervals, newInterval)

# OUTPUT
print("Inserted Intervals:", result)



#OPTIONAL CODE FOR BETTER UNDERSTANDING 

# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
#         # STORE FINAL INTERVALS
#         answer = []

#         # GET START AND END OF NEW INTERVAL
#         new_start = newInterval[0]
#         new_end = newInterval[1]

#         # CHECK EACH EXISTING INTERVAL
#         for start, end in intervals:

#             # CASE 1:
#             # CURRENT INTERVAL IS COMPLETELY BEFORE NEW INTERVAL
#             if end < new_start:
#                 # ADD CURRENT INTERVAL
#                 answer.append([start, end])

#             # CASE 2:
#             # CURRENT INTERVAL IS COMPLETELY AFTER NEW INTERVAL
#             elif start > new_end:
#                 # ADD NEW INTERVAL BEFORE CURRENT INTERVAL
#                 answer.append([new_start, new_end])

#                 # ADD CURRENT INTERVAL
#                 answer.append([start, end])

#                 # ADD ALL REMAINING INTERVALS
#                 # THEY ARE ALSO AFTER NEW INTERVAL
#                 index = intervals.index([start, end])
#                 answer.extend(intervals[index + 1:])

#                 # NEW INTERVAL IS ALREADY INSERTED
#                 return answer

#             # CASE 3:
#             # CURRENT INTERVAL OVERLAPS WITH NEW INTERVAL
#             else:
#                 # TAKE THE LEFTMOST START
#                 new_start = min(new_start, start)

#                 # TAKE THE RIGHTMOST END
#                 new_end = max(new_end, end)

#         # ADD NEW INTERVAL
#         # THIS ALSO HANDLES THE CASE WHERE
#         # NEW INTERVAL BELONGS AT THE END
#         answer.append([new_start, new_end])

#         # RETURN FINAL INTERVALS
#         return answer