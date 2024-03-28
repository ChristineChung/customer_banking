#customer_banking

"""In the customer_banking.py file, you will import the create_savings_account and 
create_cd_account functions, then create a main function that prompts the user to 
enter the savings and CD account details, call the corresponding functions to calculate 
the interest earned and update the balances, and display the results."""

from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt user to enter savings account details
    print("Enter Savings Account Details:")
    savings_account_number = input("Enter account number: ")
    savings_initial_balance = float(input("Enter initial balance: "))
    savings_interest_rate = float(input("Enter interest rate: "))
    
    # Create a savings account and calculate interest earned
    savings_balance, savings_interest_earned = create_savings_account(savings_account_number, savings_initial_balance, savings_interest_rate)
    
    # Display results for the savings account
    print(f"\nSavings Account Balance after interest: ${savings_balance:.2f}")
    print(f"Interest Earned on Savings Account: ${savings_interest_earned:.2f}")

    # Prompt user to enter CD account details
    print("\nEnter CD Account Details:")
    cd_account_number = input("Enter account number: ")
    cd_initial_balance = float(input("Enter initial balance: "))
    cd_interest_rate = float(input("Enter interest rate: "))
    cd_term_length = int(input("Enter CD term length in years: "))
    
    # Create a CD account and calculate interest earned
    cd_balance, cd_interest_earned = create_cd_account(cd_account_number, cd_initial_balance, cd_interest_rate, cd_term_length)
    
    # Display results for the CD account
    print(f"\nCD Account Balance after interest: ${cd_balance:.2f}")
    print(f"Interest Earned on CD Account: ${cd_interest_earned:.2f}")

if __name__ == "__main__":
    main()

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

    # Calculate interest earned
    interest_earned = savings_account.balance * savings_account.interest_rate

    # Update the account balance with the earned interest
    new_balance = savings_account.balance + interest_earned
    savings_account.set_balance(new_balance)

    return savings_account.balance, interest_earned
