import abc

class BankAccount(object):
    def __init__(self, money):
        self.money = money

    def available_amount(self):
        return self.money

    @abc.abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount < 0:
            raise Exception("You can't lose money by depositing!")
        else:
            self.money += amount

    def __str__(self):
        return("Account: {} SEK".format(self.money))


class SavingsAccount(BankAccount):
    def __init__(self, money):
        super().__init__(money)

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("You can't add money by withdrawing!")
        if amount > self.money:
            raise OverdraftException("Order cannot be completed, insufficient funds on account: " + str(self.money) +
                                    " < " + str(amount))
        else:
            self.money -= amount

class DepositAccount(BankAccount):
    MAX_OVERDRAFT = 5000
    OVERDRAFT_FEE_PERCENTAGE = 0.1

    def __init__(self, money):
        super().__init__(money)

    def withdraw(self, amount):
        if amount < 0:
            raise Exception("You can't add money by withdrawing!")
        overdraft_amount = amount - self.money
        if overdraft_amount > 0:
            if overdraft_amount > DepositAccount.MAX_OVERDRAFT:
                raise OverdraftException("Order cannot be completed, will go over overdraft limit: " + 
                                          str(self.money) + " - " + str(amount) + " < -" +
                                          str(DepositAccount.MAX_OVERDRAFT))
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
except OverdraftException as ex:
        print("  ", ex)


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
except OverdraftException as ex:
        print("  ", ex)
print(account)
account.apply_overdraft_fee()
print(account)
