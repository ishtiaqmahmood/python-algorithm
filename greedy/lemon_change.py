def lemonade_change(bills):
    """
    Determines if change can be provided for each customer.

    Args:
        bills (list): Bills provided by each customer.

    Returns:
        bool: True if change can be provided, False otherwise.
    """
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if not five:
                return False
            five -= 1
            ten += 1
        else: # bill == 20
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


if __name__ == "__main__":
    test_bills = [5, 5, 5, 10, 20]
    print(f"Can provide change for {test_bills}: {lemonade_change(test_bills)}")
