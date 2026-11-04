#PREVIOUS PERMUTATION WITH ONE SWAP


def prevPermOpt1(arr):

    # Step 1: Initialize pivot
    pivot = -1

    # Step 2: Find pivot from right to left
    for i in range(len(arr) - 2, -1, -1):

        # Find the first position where current > next
        if arr[i] > arr[i + 1]:
            pivot = i
            break

    # If no pivot exists, return the original array
    if pivot == -1:
        return arr

    # Step 3: Find the largest element smaller than pivot
    j = len(arr) - 1

    while arr[j] >= arr[pivot]:
        j -= 1

    # Step 4: Handle duplicate candidate values
    # Choose the leftmost occurrence of the candidate
    while j > pivot + 1 and arr[j] == arr[j - 1]:
        j -= 1

    # Step 5: Swap pivot and candidate
    arr[pivot], arr[j] = arr[j], arr[pivot]

    # Step 6: Return the previous permutation
    return arr


# Example input
arr = [3, 1, 1, 3]

# Function call
answer = prevPermOpt1(arr)

# Display result
print("Previous Permutation:", answer)
