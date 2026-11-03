#GAS STATION


def canCompleteCircuit(gas, cost):

    # Step 1: Initialize variables
    current_tank = 0
    total_tank = 0
    start = 0

    # Step 2: Traverse all gas stations
    for i in range(len(gas)):

        # Calculate gas gained or consumed
        difference = gas[i] - cost[i]

        # Update both tank balances
        current_tank += difference
        total_tank += difference

        # Step 3: Check whether the current starting point is invalid
        if current_tank < 0:

            # Try the next gas station as the starting point
            start = i + 1

            # Reset current gas for the new starting point
            current_tank = 0

    # Step 4: Check whether completing the circuit is possible
    if total_tank < 0:
        return -1

    # Return the valid starting station index
    return start


# --------------------------------
# Main Program (VS Code Execution)
# --------------------------------

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

result = canCompleteCircuit(gas, cost)

print("Gas:", gas)
print("Cost:", cost)
print("Starting Gas Station Index:", result)
