#JUMP GAME II


def jump(nums: list[int]) -> int:

    # Count the number of jumps
    jumps = 0

    # End of the range covered by the current jump
    current_end = 0

    # Farthest index reachable within the current range
    farthest = 0

    # Traverse all indices except the last one
    for i in range(len(nums) - 1):

        # Update the farthest index reachable from this range
        farthest = max(farthest, i + nums[i])

        # When we reach the end of the current jump range
        if i == current_end:

            # We must take another jump
            jumps += 1

            # Update the boundary for the next jump
            current_end = farthest

            # Stop if the last index is reachable
            if current_end >= len(nums) - 1:
                break

    # Return the minimum number of jumps
    return jumps


# Test the function
nums = [2, 3, 1, 1, 4]

result = jump(nums)

print("Input array:", nums)
print("Minimum jumps:", result)
