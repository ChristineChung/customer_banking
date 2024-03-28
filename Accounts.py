#Accounts 

class Account:
    """
    The Account class represents a basic bank account.
    """
    def __init__(self, account_number, balance=0.0, apr=0.0, months=12):
        """
        Initializes a new Account object.

        Args:
            account_number (str): The unique identifier for the account.
            balance (float, optional): The initial balance of the account. Defaults to 0.0.
            apr (float, optional): The annual percentage rate (APR) for the account. Defaults to 0.0.
            months (int, optional): The number of months for the interest calculation. Defaults to 12 (yearly).
        """
        self.account_number = account_number
        self.balance = balance
        self.apr = apr
        self.months = months

    def set_balance(self, new_balance):
        """
        Sets the balance of the account.

        Args:
            new_balance (float): The new balance for the account.
        """
        self.balance = new_balance

    def set_apr(self, new_apr):
        """
        Sets the annual percentage rate (APR) for the account.

        Args:
            new_apr (float): The new APR for the account.
        """
        self.apr = new_apr

    def set_months(self, new_months):
        """
        Sets the number of months for the interest calculation.

        Args:
            new_months (int): The new number of months for the interest calculation.
        """
        self.months = new_months

    def calculate_interest(self):
        """
        Calculates the interest earned on the account balance.

        Returns:
            float: The interest earned.
        """
        return self.balance * (self.apr / 100 * self.months / 12)

    def __str__(self):
        """
        Returns a string representation of the Account object.
        """
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}, APR: {self.apr:.2%}, Months: {self.months}"
