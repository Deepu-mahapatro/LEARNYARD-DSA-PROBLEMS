#JUMP GAME VI

from collections import deque
class Solution:
    def maxResult(self, nums, k):
        # LENGTH OF THE ARRAY
        n = len(nums)
        # DP ARRAY
        # dp[i] STORES THE MAXIMUM SCORE
        # WE CAN GET WHEN WE REACH INDEX i
        dp = [0] * n
        # STARTING POSITION
        dp[0] = nums[0]
        # CREATE A DEQUE
        # WE STORE INDEXES IN THIS DEQUE
        # THE FRONT OF THE DEQUE WILL ALWAYS CONTAIN
        # THE INDEX WITH THE MAXIMUM DP VALUE
        dq = deque([0])
        # GO THROUGH THE ARRAY FROM INDEX 1
        for i in range(1, n):
            # REMOVE INDEXES THAT ARE OUTSIDE
            # THE CURRENT JUMP RANGE
            # WE CAN ONLY JUMP FROM THE PREVIOUS K POSITIONS
            while dq and dq[0] < i - k:
                dq.popleft()
            # THE FRONT INDEX HAS THE BEST SCORE
            # AMONG THE POSITIONS WE CAN JUMP FROM
            dp[i] = nums[i] + dp[dq[0]]
            # REMOVE SMALLER DP VALUES FROM THE BACK
            # IF THE CURRENT DP VALUE IS GREATER,
            # THE OLDER SMALLER VALUE WILL NOT BE USEFUL
            # FOR FUTURE JUMPS
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            # ADD THE CURRENT INDEX TO THE DEQUE
            dq.append(i)
        # RETURN THE MAXIMUM SCORE AT THE LAST INDEX
        return dp[n - 1]

obj = Solution()

nums = [1, -1, -2, 4, -7, 3]
k = 2

result = obj.maxResult(nums, k)

print("Nums:", nums)
print("K:", k)
print("Maximum Score:", result)