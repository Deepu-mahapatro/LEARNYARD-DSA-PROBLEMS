#MICE AND CHEESE 


class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:

        # Step 1: Calculate the initial total reward
        # Assume Mouse 2 eats all the cheese
        total_reward = sum(reward2)

        # Step 2: Calculate the reward differences
        # Difference = Mouse 1 reward - Mouse 2 reward
        differences = []

        for i in range(len(reward1)):
            differences.append(reward1[i] - reward2[i])

        # Step 3: Sort differences in descending order
        # The largest differences give the maximum additional reward
        differences.sort(reverse=True)

        # Step 4: Select the k largest differences
        # Assign these k cheese pieces to Mouse 1
        for i in range(k):
            total_reward += differences[i]

        # Step 5: Return the maximum combined reward
        return total_reward


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.miceAndCheese([1, 1, 3, 4], [3, 4, 1, 1], 2))
# Output: 14

print(obj.miceAndCheese([1, 1], [1, 1], 2))
# Output: 2
