#DIVIDE ARRAY IN SETS OF K CONSECUTIVE NUMBERS 


from collections import Counter


def isPossibleDivide(nums, k):

    # Step 1: Check whether the array can be divided into groups of size k
    if len(nums) % k != 0:
        return False

    # Step 2: Sort the array in ascending order
    nums.sort()

    # Step 3: Create a frequency Hash Map
    freq = Counter(nums)

    # Step 4: Traverse unique numbers in ascending order
    for num in sorted(freq):

        # Check whether the current number is still available
        if freq[num] > 0:

            # Number of groups that must start with this number
            count = freq[num]

            # Step 5: Find the remaining consecutive numbers
            for j in range(1, k):

                # Generate the next consecutive number
                next_num = num + j

                # Check whether enough occurrences are available
                if freq[next_num] < count:
                    return False

                # Consume the required occurrences
                freq[next_num] -= count

            # All occurrences of the starting number are now consumed
            freq[num] = 0

    # All numbers have been divided successfully
    return True


# Example 1
nums = [1, 2, 3, 6, 2, 3, 4, 7, 8]
k = 3

answer = isPossibleDivide(nums, k)

print("Can divide into consecutive groups:", answer)
