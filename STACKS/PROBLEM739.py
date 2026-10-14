#DAILY TEMPERATURES 

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        n = len(temperatures)

        # STORE THE NUMBER OF DAYS TO WAIT FOR EACH DAY
        result = [0] * n

        # STORE INDICES OF DAYS WHOSE WARMER DAY IS NOT FOUND
        stack = []

        # CHECK EACH DAY'S TEMPERATURE
        for i in range(n):

            # CURRENT TEMPERATURE IS WARMER THAN THE STACK TOP
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # GET THE PREVIOUS DAY'S INDEX
                previous_day = stack.pop()

                # CALCULATE HOW MANY DAYS WE WAITED
                result[previous_day] = i - previous_day

            # STORE THE CURRENT DAY'S INDEX IN THE STACK
            stack.append(i)

        # RETURN THE FINAL ANSWER
        return result


# INPUT
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# CREATE OBJECT AND CALL THE METHOD
obj = Solution()
output = obj.dailyTemperatures(temperatures)

# OUTPUT
print(output)