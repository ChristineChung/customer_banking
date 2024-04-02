# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    balance = float(input('What is your balance? '))    
    interest = float(input('What is your interest rate? '))
    months = int(input('How many months? '))
    
    #new_balance = balance + interest_earned

    # Call the create_savings_account function and pass the variables from the user.
    balance, interest_earned = create_savings_account(balance, interest, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nSavings Account Balance after interest: ${balance:.2f}")
    print(f"Interest Earned on Savings Account: ${interest_earned:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("\nEnter CD Account Details:")
    cd_account = (input("Enter initial balance: "))
    cd_interest_rate = float(input("Enter interest rate: "))
    cd_months = int(input("Enter CD term length in months: "))

    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_account, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"\nSavings Account Balance after interest: ${cd_updated_balance:.2f}")
    print(f"Interest Earned on Savings Account: ${cd_interest_earned:.2f}")

    # Call the main function

if __name__ == "__main__":
    main()