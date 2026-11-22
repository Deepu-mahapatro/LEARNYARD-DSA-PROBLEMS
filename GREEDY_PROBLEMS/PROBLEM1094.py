#CAR POOLING 


class Solution:
    def carPooling(self, trips, capacity):

        # Step 1: Create a difference array
        # Locations are between 0 and 1000
        passengers = [0] * 1001

        # Step 2: Process each trip
        for count, start, end in trips:

            # Passengers enter the car at the pickup location
            passengers[start] += count

            # Passengers leave the car at the drop-off location
            passengers[end] -= count

        # Step 3: Calculate the running passenger count
        current_passengers = 0

        for count in passengers:

            # Update the current number of passengers
            current_passengers += count

            # Check whether car capacity is exceeded
            if current_passengers > capacity:
                return False

        # Step 4: All trips completed within capacity
        return True


# Test cases
obj = Solution()

print(obj.carPooling([[2, 1, 5], [3, 3, 7]], 4))  # False
print(obj.carPooling([[2, 1, 5], [3, 5, 7]], 3))  # True
print(obj.carPooling([[2, 2, 5], [3, 5, 7]], 3))  # True
