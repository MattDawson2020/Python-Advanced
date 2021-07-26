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


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):
        self.balance -= (amount * self.fee)


acc=Checking("balance.txt", 0.05)
acc.deposit(500)
print(acc.balance)
acc.transfer(50)
print(acc.balance)