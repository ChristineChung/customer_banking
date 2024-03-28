#cd_account

from Accounts import Account

def create_cd_account(account_number, initial_balance, apr, months):
    """
    Create a CD account instance, calculate interest earned based on user input,
    update the account balance with the earned interest, and return the updated balance and interest earned.

    Args:
        account_number (str): The unique identifier for the CD account.
        initial_balance (float): The initial balance of the CD account.
        apr (float): The annual percentage rate (APR) for the CD account.
        months (int): The term length of the CD account in months.

    Returns:
        Tuple: Updated balance after adding interest and interest earned.
    """
    # Create a new CD account instance
    cd_account = Account(account_number, initial_balance, apr, months)

    # Calculate the interest earned
    interest_earned = cd_account.balance * (cd_account.apr / 100 * cd_account.months / 12)

    # Calculate the new balance after adding the interest
    new_balance = cd_account.balance + interest_earned

    # Update the account balance with the earned interest
    cd_account.set_balance(new_balance)

    return cd_account.balance, interest_earned
