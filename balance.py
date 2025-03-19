class SecretAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("у вас недостаточно денег")

account = SecretAccount(100)
print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())