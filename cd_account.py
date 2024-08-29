"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, 0, interest_rate, months)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = cd_account.calculate_interest()
    # Update the account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = cd_account.get_balance() + interest_earned
    # Return the updated balance and the interest earned
    # ADD YOUR CODE HERE
    return updated_balance, interest_earned
# Call the function with example values
# ADD YOUR CODE HERE
balance = 1000
interest_rate = 0.05
months = 12
updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)
print(f"Updated balance: ${updated_balance:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
cd_account.update_balance(cd_account.get_balance() + interest_earned)
