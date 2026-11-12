#QUEUE RECONSTRUCTION BY HEIGHT 


class Solution:
    def reconstructQueue(self, people):

        # Step 1: Sort people by height in descending order.
        # If heights are equal, sort k in ascending order.
        people.sort(key=lambda x: (-x[0], x[1]))

        # Step 2: Create an empty list to store the reconstructed queue
        result = []

        # Step 3: Iterate through each person
        for person in people:

            # Step 4: Insert the person at the index specified by k
            # person[1] represents the number of taller or equal-height
            # people who must be in front of this person
            result.insert(person[1], person)

        # Step 5: Return the reconstructed queue
        return result


# Test case
obj = Solution()

people = [
    [7, 0],
    [4, 4],
    [7, 1],
    [5, 0],
    [6, 1],
    [5, 2]
]

print(obj.reconstructQueue(people))

# Expected Output:
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
