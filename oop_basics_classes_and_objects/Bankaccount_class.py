class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
            self.show_balance()
        else:
            print("Insufficient balance!")


# Bank account objects
b1 = BankAccount(10000)
b2 = BankAccount(5000)

# Operations on b1
b1.deposit(2000)
b1.withdraw(1500)
b1.withdraw(3000)
b1.show_balance()

print()

# Operations on b2
b2.deposit(1000)
b2.withdraw(7000)
b2.show_balance()