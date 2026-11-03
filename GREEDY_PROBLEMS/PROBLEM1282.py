#GROUP THE PEOPLE GIVEN THE GROUP SIZE THEY BELONG TO 


def groupThePeople(groupSizes):

    # Dictionary to store person indices based on group size
    groups = {}

    # Stores all completed groups
    result = []

    # Traverse the groupSizes array
    for i, size in enumerate(groupSizes):

        # If this group size is not present, create an empty list
        if size not in groups:
            groups[size] = []

        # Add the current person's index to the corresponding group
        groups[size].append(i)

        # Check whether the required group size has been reached
        if len(groups[size]) == size:

            # Add the completed group to the result
            result.append(groups[size])

            # Reset the list to collect the next group of the same size
            groups[size] = []

    # Return all completed groups
    return result


# Example input
groupSizes = [3, 3, 3, 3, 3, 1, 3]

# Call the function
answer = groupThePeople(groupSizes)

# Print the result
print("Groups:", answer)
