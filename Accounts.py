""" Create a Account class with methods"""

# Define the Account class

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance
        return self.balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest_earned):
        """Sets the interest gained for the the account"""
        self.interest = interest_earned
        return self.interest_earned
