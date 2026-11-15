# MAXIMUM MATCHING OF PLAYERS WITH TRAINERS 


class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:

        # Step 1: Sort both arrays in ascending order
        players.sort()
        trainers.sort()

        # Step 2: Initialize two pointers
        i = 0  # Pointer for players
        j = 0  # Pointer for trainers

        # Step 3: Count successful matches
        matches = 0

        # Step 4: Traverse both arrays
        while i < len(players) and j < len(trainers):

            # Check if trainer can train the current player
            if players[i] <= trainers[j]:

                # Match the player with the trainer
                matches += 1

                # Move both pointers
                i += 1
                j += 1

            else:
                # Trainer capacity is insufficient
                # Try the next trainer
                j += 1

        # Step 5: Return maximum number of matches
        return matches


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.matchPlayersAndTrainers(
    [4, 7, 9], [8, 2, 5, 8]
))
# Output: 2

print(obj.matchPlayersAndTrainers(
    [1, 1, 1], [10]
))
# Output: 1

print(obj.matchPlayersAndTrainers(
    [5, 6], [1, 2, 3]
))
# Output: 0
