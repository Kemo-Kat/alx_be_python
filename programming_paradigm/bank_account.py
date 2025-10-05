
class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        Default balance is 0 if not specified.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        Returns True if withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")


