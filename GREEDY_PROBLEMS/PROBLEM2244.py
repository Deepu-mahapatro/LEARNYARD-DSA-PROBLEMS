#MINIMUM ROUNDS TO COMPLETE ALL TASKS


from collections import Counter


class Solution:
    def minimumRounds(self, tasks):

        # Step 1: Initialize total rounds
        total_rounds = 0

        # Step 2: Count frequency of each difficulty
        freq = Counter(tasks)

        # Step 3: Process each frequency
        for count in freq.values():

            # If frequency is 1, completing tasks is impossible
            if count == 1:
                return -1

            # Step 4: Calculate groups of 3 and remaining tasks
            groups = count // 3
            remaining = count % 3

            # Step 5: Calculate minimum rounds

            # Case 1: No remaining tasks
            if remaining == 0:
                total_rounds += groups

            # Case 2: One task remains
            # Replace one group of 3 with two groups of 2
            elif remaining == 1:
                total_rounds += groups - 1 + 2

            # Case 3: Two tasks remain
            # Add one extra group of 2
            else:
                total_rounds += groups + 1

        # Step 6: Return total rounds
        return total_rounds


# Test cases
obj = Solution()

print(obj.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))  # 4
print(obj.minimumRounds([2, 3, 3]))                       # -1
print(obj.minimumRounds([2, 2, 2, 2, 2]))                # 2
print(obj.minimumRounds([1, 1, 1, 1, 1, 1, 1]))          # 3
