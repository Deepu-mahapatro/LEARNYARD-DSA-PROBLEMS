#REORGANIZE STRING


from collections import Counter
import heapq


def reorganizeString(s):

    # Step 1: Calculate the length of the string
    n = len(s)

    # Step 2: Count the frequency of each character
    freq = Counter(s)

    # Step 3: Find the maximum character frequency
    max_freq = max(freq.values())

    # Step 4: Check whether rearrangement is possible
    if max_freq > (n + 1) // 2:
        return ""

    # Step 5: Create a Max Heap
    # Python provides a Min Heap, so use negative frequencies
    heap = []

    for char, count in freq.items():
        heapq.heappush(heap, (-count, char))

    # Step 6: Initialize result and previous character
    result = []
    prev = None

    # Step 7: Extract characters and rearrange them
    while heap:

        # Get the character with the highest frequency
        count, char = heapq.heappop(heap)

        # Add the character to the result
        result.append(char)

        # Decrease its frequency
        count += 1

        # Push the previous character back if it has remaining frequency
        if prev and prev[0] < 0:
            heapq.heappush(heap, prev)

        # Store the current character and its remaining frequency
        prev = (count, char)

    # Step 8: Convert the result list into a string
    return "".join(result)


# Test Case 1
s = "aab"
print("Result:", reorganizeString(s))

# Test Case 2
s = "aaab"
print("Result:", reorganizeString(s))

# Test Case 3
s = "aaabbc"
print("Result:", reorganizeString(s))
