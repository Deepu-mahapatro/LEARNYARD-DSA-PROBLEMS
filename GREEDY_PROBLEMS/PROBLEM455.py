#ASSIGN COOKIES 



def findContentChildren(g: list[int], s: list[int]) -> int:

    # Sort greed factors and cookie sizes in ascending order
    g.sort()
    s.sort()

    # i tracks the current child
    # j tracks the current cookie
    i = 0
    j = 0

    # Count the number of satisfied children
    satisfied = 0

    # Traverse while children and cookies are available
    while i < len(g) and j < len(s):

        # If this cookie satisfies the current child
        if s[j] >= g[i]:

            # Assign the cookie and satisfy the child
            satisfied += 1

            # Move to the next child
            i += 1

        # Move to the next cookie in either case
        j += 1

    # Return the maximum number of satisfied children
    return satisfied


# Test the function
g = [1, 2, 3]
s = [1, 1]

result = findContentChildren(g, s)

print("Greed factors:", g)
print("Cookie sizes:", s)
print("Satisfied children:", result)
