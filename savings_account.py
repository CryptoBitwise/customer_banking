"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# END ADD YOUR CODE HERE
# Import the unittest module.
import unittest

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
    account = Account(balance, 0, interest_rate)

    interest_earned = account.calculate_interest(months)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = account.update_balance(interest_earned)
    # Return the updated savings account balance and the interest earned.
    # ADD YOUR CODE HERE
    return updated_balance, interest_earned
# Define a function for the Checking Account
def create_checking_account(balance, overdraft_limit, fees):

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account = Account(balance, overdraft_limit, fees)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
# Define a function for the Credit Card Account
def create_credit_card_account(balance, credit_limit, interest_rate, fees):
   # Create an instance of the `Account` class and pass in the balance, credit limit,
   # interest rate, and fees parameters.
   account = Account(balance, credit_limit, interest_rate, fees)
   # Return the instance of the `Account` class.
   return account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
   # Create an instance of the `Account` class and pass in the balance, interest rate,
   # and months parameters.
   account = Account(balance, interest_rate, months)
   # Return the instance of the `Account` class.
   return account
# Define a function for the Checking Account
def create_checking_account(balance, overdraft_limit, fees):
   # Create an instance of the `Account` class and pass in the balance, overdraft limit
   # and fees parameters.
   account = Account(balance, overdraft_limit, fees)
   # Return the instance of the `Account` class.
   return account
