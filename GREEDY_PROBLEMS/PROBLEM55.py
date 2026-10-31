#JUMP GAME 


def canJump(nums: list[int]) -> bool:

    # Track the farthest index we can reach
    farthest = 0

    # Traverse the array from the first index
    for i in range(len(nums)):

        # If the current index is beyond our reach,
        # we cannot continue
        if i > farthest:
            return False

        # Update the farthest reachable index
        farthest = max(farthest, i + nums[i])

        # If we can reach the last index, return True
        if farthest >= len(nums) - 1:
            return True

    # The last index is reachable
    return True


# Test the function
nums = [2, 3, 1, 1, 4]

result = canJump(nums)

print("Input array:", nums)
print("Can reach the last index:", result)
