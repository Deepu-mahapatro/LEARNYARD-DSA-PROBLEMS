#BOATS TO SAVE PEOPLE 


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        # Step 1: Sort people by weight in ascending order
        people.sort()

        # Step 2: Initialize two pointers
        left = 0                    # Lightest person
        right = len(people) - 1     # Heaviest person

        # Step 3: Initialize boat counter
        boats = 0

        # Step 4: Traverse using two pointers
        # Use <= to handle the last remaining person
        while left <= right:

            # Check whether the lightest and heaviest
            # people can fit together in one boat
            if people[left] + people[right] <= limit:

                # Both people can share one boat
                left += 1

            # The heaviest person always gets a boat
            right -= 1

            # Count the boat used
            boats += 1

        # Step 5: Return minimum number of boats
        return boats


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.numRescueBoats([1, 2], 3))
# Output: 1

print(obj.numRescueBoats([3, 2, 2, 1], 3))
# Output: 3

print(obj.numRescueBoats([3, 5, 3, 4], 5))
# Output: 4

print(obj.numRescueBoats([1, 1, 2, 2], 3))
# Output: 2
