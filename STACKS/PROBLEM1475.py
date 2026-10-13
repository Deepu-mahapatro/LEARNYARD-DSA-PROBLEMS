#FINAL PRICES WITH A SPECIAL DISCOUNT IN A SHOP 


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # COPY PRICES TO STORE THE FINAL PRICES
        answer = prices.copy()
        # STACK STORES INDICES OF ITEMS WAITING FOR A DISCOUNT
        stack = []
        # TRAVERSE THROUGH EACH PRICE
        for i in range(len(prices)):#SUBTRACT 
            # CHECK IF CURRENT PRICE IS LESS THAN OR EQUAL TO
            # THE PRICE OF THE ITEM AT THE TOP OF THE STACK
            while stack and prices[stack[-1]] >= prices[i]:
                # GET THE INDEX OF THE PREVIOUS ITEM
                index = stack.pop()
                # SUBTRACT CURRENT PRICE AS ITS DISCOUNT
                answer[index] = prices[index] - prices[i]
            # STORE CURRENT INDEX FOR A FUTURE DISCOUNT
            stack.append(i)
        # RETURN FINAL PRICES
        return answer


# INPUT
prices = [8, 4, 6, 2, 3]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.finalPrices(prices)

# OUTPUT
print("Final Prices:", result)
