#SUPER WASHING MACHINES 

class Solution:
    def findMinMoves(self, machines: list[int]) -> int:

        # Step 1: Get the number of washing machines
        n = len(machines)

        # Step 2: Calculate the total number of dresses
        total = sum(machines)

        # Step 3: Check whether equal distribution is possible
        if total % n != 0:
            return -1

        # Step 4: Calculate the target dresses per machine
        target = total // n

        # Step 5: Initialize tracking variables
        balance = 0
        max_moves = 0

        # Step 6: Traverse all washing machines
        for load in machines:

            # Calculate the surplus or deficit of current machine
            diff = load - target

            # Update cumulative balance
            balance += diff

            # Calculate maximum moves required
            max_moves = max(
                max_moves,
                abs(balance),
                diff
            )

        # Step 7: Return minimum moves required
        return max_moves


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.findMinMoves([1, 0, 5]))
# Output: 3

print(obj.findMinMoves([0, 2, 0]))
# Output: -1

print(obj.findMinMoves([0, 3, 0]))
# Output: 2

print(obj.findMinMoves([1, 1, 1]))
# Output: 0

print(obj.findMinMoves([0, 0, 6, 0, 0]))
# Output: 4
