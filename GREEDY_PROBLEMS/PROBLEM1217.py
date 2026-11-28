#MINIMUM COST TO MOVE CHIPS TO THE SAME POSITION 


def minCostToMoveChips(position: list[int]) -> int:

    # Count chips at odd and even positions
    odd = 0
    even = 0

    # Traverse all chip positions
    for pos in position:

        # If the position is odd
        if pos % 2 != 0:
            odd += 1

        # Otherwise, the position is even
        else:
            even += 1

    # Moving chips within the same parity costs zero.
    # Choose the group with fewer chips to move.
    return min(odd, even)


# Test the function
position = [2, 2, 3, 3, 3, 4]

result = minCostToMoveChips(position)

print("Chip positions:", position)
print("Minimum cost:", result)
