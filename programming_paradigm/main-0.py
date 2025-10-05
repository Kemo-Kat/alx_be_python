# main-0.py
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with $100 as per example
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()  # Show updated balance after deposit
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
            account.display_balance()  # Show updated balance after successful withdrawal
        else:
            print("Insufficient funds.")
            account.display_balance()  # Show current balance even when withdrawal fails
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
