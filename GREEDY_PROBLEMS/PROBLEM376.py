#WIGGLE SUBSEQUENCE 


def wiggleMaxLength(nums):

    # Stores the length of the longest wiggle subsequence
    count = 1

    # Stores the previous non-zero difference
    prev_diff = 0

    # Traverse the array starting from index 1
    for i in range(1, len(nums)):

        # Calculate the difference between current and previous elements
        diff = nums[i] - nums[i - 1]

        # If both elements are equal, skip this iteration
        if diff == 0:
            continue

        # Check for an upward movement
        # Previous direction must be downward or have no direction
        if diff > 0 and prev_diff <= 0:

            # Increase the wiggle subsequence length
            count += 1

            # Update the previous difference
            prev_diff = diff

        # Check for a downward movement
        # Previous direction must be upward or have no direction
        elif diff < 0 and prev_diff >= 0:

            # Increase the wiggle subsequence length
            count += 1

            # Update the previous difference
            prev_diff = diff

    # Return the maximum wiggle subsequence length
    return count


# Example input
nums = [1, 7, 4, 9, 2, 5]

# Function call
result = wiggleMaxLength(nums)

# Print the result
print("Maximum Wiggle Subsequence Length:", result)
