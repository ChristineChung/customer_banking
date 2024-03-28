# customer_banking
module 3 challenge

Sure, here's a README.md file for the customer banking code:

# Customer Banking Application

This is a Python-based customer banking application that allows users to create and manage savings and CD (Certificate of Deposit) accounts.

## Features

1. **Savings Account Management**:
   - Create a savings account with an account number, initial balance, and interest rate.
   - Calculate the interest earned on the savings account based on the balance and interest rate.
   - Update the savings account balance with the earned interest.

2. **CD Account Management**:
   - Create a CD account with an account number, initial balance, annual percentage rate (APR), and term length (in months).
   - Calculate the interest earned on the CD account based on the balance, APR, and term length.
   - Update the CD account balance with the earned interest.

3. **User Interface**:
   - Prompt the user to enter the details for the savings and CD accounts.
   - Display the updated balances and interest earned for both the savings and CD accounts.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-username/customer-banking.git
   ```

2. Navigate to the project directory:
   ```
   cd customer-banking
   ```

3. Run the `customer_banking.py` file to start the application:
   ```
   python customer_banking.py
   ```

## File Structure

- `Accounts.py`: Contains the `Account` class, which represents a basic bank account.
- `savings_account.py`: Defines the `create_savings_account` function to manage savings accounts.
- `cd_account.py`: Defines the `create_cd_account` function to manage CD accounts.
- `customer_banking.py`: The main entry point of the application, which prompts the user for account details and displays the results.

## Dependencies

This application does not have any external dependencies. It uses only the standard Python library.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
