#PATCHING ARRAY 


def minPatches(nums, n):
    # Sort the array so we can process numbers in ascending order
    nums.sort()

    # Smallest number that we cannot currently form
    miss = 1

    # Pointer to track the current array element
    i = 0

    # Count the number of patches added
    patches = 0

    # Continue until we can form every number from 1 to n
    while miss <= n:

        # Case 1: An existing number can extend our reachable range
        if i < len(nums) and nums[i] <= miss:

            # Use the current number to extend the range
            miss += nums[i]

            # Move to the next array element
            i += 1

        else:
            # Case 2: We cannot form 'miss'
            # So, add 'miss' itself as a patch
            patches += 1

            # Adding 'miss' doubles our reachable range
            miss += miss

    # Return the minimum number of patches required
    return patches


# Main function: Test the solution
if __name__ == "__main__":
    nums = [1, 2, 5]
    n = 10

    result = minPatches(nums, n)

    print("Minimum patches required:", result)
