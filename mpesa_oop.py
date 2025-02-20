
class User :
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.account=Account(self)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number}'

class Account :

    def __init__(self, user):
        self.user = user
        self.balance = 0.0
    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited.New balance: {self.balance}")

        else:
            print(f"Deposited amount must be positive.")

    def __repr__(self):
        return f'Account{self.user.first_name} {self.user.last_name} {self.balance}'
        #representation of Account
    def withdraw(self, amount):

        if 0< amount <= self.balance:   #check if withdrawal amount is valid
            self.balance -= amount
            print(f"{amount} withdrawn.New balance: {self.balance}")

        else:
            print(f"Insufficient balance.")

    def __rep__(self):
        return f'Account{self.user.first_name} {self.user.last_name} {self.balance}'

# define a transaction class

class transaction :
    def __init__(self,account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print(f"Invalid transaction type.")
    def __repr__(self):
        return f"Transaction(Account: {self.account.user.first_name},{self.account.user.last_name} Amount: {self.amount}, Type: {self.transaction_type})"

# example usage == object

user1=User(first_name="John",last_name="Smith",email="johnsmith@gmail.com",phone_number="718789441")
print(user1)

# deposit amount
user1.account.deposit(1500)
user1.account.withdraw(300)
transaction1=transaction(user1.account,600,"deposit")
transaction1.process()

transaction2=transaction(user1.account,200,"withdraw")
transaction2.process()

print(user1.account)

user2=User(first_name='Amy',last_name='Pendo',email="amypendo44@gmail.com",phone_number="7987456241")
print(user2)

user2.account.deposit(2000)
user2.account.withdraw(600)

transaction1=transaction(user2.account,200,"withdraw")
transaction1.process()

transaction2=transaction(user2.account,600,"deposit")
transaction2.process()

