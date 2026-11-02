#LEMONADE CHANGE


def lemonadeChange(bills):

    # Track the number of $5 and $10 bills
    five = 0
    ten = 0

    # Process each customer's payment
    for i in range(len(bills)):

        # Case 1: Customer pays $5
        # No change is required
        if bills[i] == 5:
            five += 1

        # Case 2: Customer pays $10
        # We must return $5 as change
        elif bills[i] == 10:

            if five > 0:
                five -= 1
                ten += 1

            else:
                # No $5 bill available for change
                return False

        # Case 3: Customer pays $20
        # We must return $15 as change
        elif bills[i] == 20:

            # Prefer $10 + $5
            # This preserves smaller $5 bills
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1

            # If $10 + $5 is unavailable,
            # use three $5 bills
            elif five >= 3:
                five -= 3

            else:
                # Cannot provide $15 change
                return False

    # All customers received correct change
    return True


# -------------------------------
# Main Program (VS Code Execution)
# -------------------------------

bills = [5, 5, 5, 10, 20]

result = lemonadeChange(bills)

print("Bills:", bills)
print("Can provide change to all customers:", result)
