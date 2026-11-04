#PARTITION LABELS


def partitionLabels(s):

    # Step 1: Store the last occurrence of each character
    last = {}

    for i in range(len(s)):
        last[s[i]] = i

    # Step 2: Initialize variables
    start = 0
    end = 0
    result = []

    # Step 3: Traverse the string
    for i in range(len(s)):

        # Find the farthest last occurrence
        # among the characters encountered so far
        end = max(end, last[s[i]])

        # Step 4: Check if the current partition is complete
        if i == end:

            # Calculate and store partition length
            result.append(end - start + 1)

            # Start the next partition
            start = i + 1

    # Step 5: Return partition lengths
    return result


# Example input
s = "ababcbacadefegdehijhklij"

# Function call
answer = partitionLabels(s)

# Print result
print("Partition lengths:", answer)
