"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# END ADD YOUR CODE HERE

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account = Account(balance, 0)

    interest_earned = balance *  (interest_rate / 100) * (months/12)
    updated_balance =  balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)

    return updated_balance, interest_earned