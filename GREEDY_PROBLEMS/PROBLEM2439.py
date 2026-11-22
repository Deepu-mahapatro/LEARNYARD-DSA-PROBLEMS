#MINIMIZE MAXIMIZE ARRAY 

def minimizeArrayValue(nums):

    # Stores the cumulative sum of elements
    prefix_sum = 0

    # Stores the minimum possible maximum value
    result = 0

    # Traverse the array
    for i in range(len(nums)):

        # Add the current element to the prefix sum
        prefix_sum += nums[i]

        # Calculate the ceiling average of the current prefix
        current_max = (prefix_sum + i) // (i + 1)

        # Update the maximum ceiling average
        result = max(result, current_max)

    # Return the minimum possible maximum value
    return result


# Input from the user
nums = list(map(int, input("Enter array elements: ").split()))

# Call the function
answer = minimizeArrayValue(nums)

# Print the result
print("Minimum possible maximum value:", answer)