#savings_account

from Accounts import Account

def create_savings_account(account_number, initial_balance, interest_rate):
    """
    Create a savings account instance, calculate interest earned based on user input,
    update the account balance with the earned interest, and return the updated balance and interest earned.

    Args:
        account_number (str): The unique identifier for the savings account.
        initial_balance (float): The initial balance of the savings account.
        interest_rate (float): The interest rate for the savings account.

    Returns:
        Tuple: Updated balance after adding interest and interest earned.
    """
    # Create a new savings account instance
    savings_account = Account(account_number, initial_balance, interest_rate)

    # Get user input for the interest earned
    interest_earned = float(input("Enter the interest earned: "))

    # Calculate new balance after adding interest
    new_balance = savings_account.balance + interest_earned

    # Update the account balance with the earned interest
    savings_account.set_balance(new_balance)

    return savings_account.balance, interest_earned
