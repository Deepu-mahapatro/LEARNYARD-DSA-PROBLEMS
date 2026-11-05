#CONSTRUCT K PALINDROME STRINGS 


from collections import Counter


def canConstruct(s, k):

    # Step 1: Calculate the length of the string
    n = len(s)

    # Step 2: Check whether enough characters are available
    if n < k:
        return False

    # Step 3: Count the frequency of each character
    freq = Counter(s)

    # Step 4: Initialize odd frequency counter
    odd_count = 0

    # Step 5: Count the odd frequencies
    for count in freq.values():

        if count % 2 != 0:
            odd_count += 1

    # Step 6: Check whether k palindromes are possible
    if odd_count <= k:
        return True
    else:
        return False


# Test Case 1
s = "annabelle"
k = 2
print(canConstruct(s, k))


# Test Case 2
s = "leetcode"
k = 3
print(canConstruct(s, k))


# Test Case 3
s = "aabb"
k = 1
print(canConstruct(s, k))
