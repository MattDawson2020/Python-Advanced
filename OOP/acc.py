class Account:
    # example account uses a txt file for an external account, which is unrealistic, usually would be a DB
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        self.commit()

    def deposit(self, amount):
        self.balance += amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


account=Account("balance.txt")
print(account)
print(account.balance)

account.withdraw(500)
print(account.balance)

account.deposit(2000)
print(account.balance)

