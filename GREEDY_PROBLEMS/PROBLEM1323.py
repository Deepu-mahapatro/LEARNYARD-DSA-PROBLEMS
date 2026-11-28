#MAXIMUM 69 NUMBER 


class Solution:
    def maximum69Number(self, num: int) -> int:

        # Convert the integer into a list of digits
        digits = list(str(num))

        # Traverse each digit from left to right
        for i in range(len(digits)):

            # Check if the current digit is 6
            if digits[i] == '6':

                # Replace the first 6 with 9
                digits[i] = '9'

                # Stop after one replacement
                break

        # Convert the list back into an integer
        return int(''.join(digits))


# Create an object of the Solution class
obj = Solution()

# Take input from the user
num = int(input("Enter a number: "))

# Call the method and display the result
result = obj.maximum69Number(num)

print("Maximum number:", result)
