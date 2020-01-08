import abc

class BankAccount(object):
    def __init__(self, dineros):
        self.money = dineros

    def available_amount(self):
        return self.money

    @abc.abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount < 0:
            raise Exception("u cant lose money by depositing wtf u thinking")
        else:
            self.money += amount

    def __str__(self):
        return("Account: {} SEK".format(self.money))


class SavingsAccount(BankAccount):
    def __init__(self, dineros):
        super().__init__(dineros)
        self.overdraft = 0.0

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("u cant add money by withdrawing wtf u thinking")
        if amount > self.money:
            raise OverdraftException("Order cannot be completed, insufficient funds on account")
        else:
            self.money -= amount

class DepositAccount(BankAccount):
    MAX_OVERDRAFT = 5000
    OVERDRAFT_FEE_PERCENTAGE = 0.1
    def __init__(self, dineros):
        super().__init__(dineros)

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("u cant add money by withdrawing wtf u thinking")
        overdraft_amount = amount - self.money
        if overdraft_amount > 0:
            if overdraft_amount > DepositAccount.MAX_OVERDRAFT:
                raise OverdraftException("Order cannot be completed, will go over overdraft limit")
            else:
                self.money -= amount

    def apply_overdraft_fee(self):
        self.money += min(0, self.money) * DepositAccount.OVERDRAFT_FEE_PERCENTAGE
        # Hope no exception occurs in between here or customer will be sad
        self.overdraft = 0.0


class OverdraftException(Exception):
    pass

account = SavingsAccount(1500)
print(account)
account.deposit(400)
print(account)
try:
    account.withdraw(2000)
except OverdraftException:
        print("yep")


account = DepositAccount(1500)
print(account)
account.deposit(400)
print(account)
account.apply_overdraft_fee()
print(account)
account.withdraw(2000)
print(account)
try:
    account.withdraw(5000)
except OverdraftException:
        print("yep")
print(account)
account.apply_overdraft_fee()
print(account)