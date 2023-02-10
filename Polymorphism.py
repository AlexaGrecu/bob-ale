class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, value):
        self.__balance = self.__balance + value

        print('Deposit amount:', value)
        print('Balance after deposit:', self.__balance)

    def withdrawal(self, value):
        self.__balance = self.__balance - value

        print('Withdrawal amount:', value)
        print('Balance after withdrawal:', self.__balance)


b_1 = BankAccount(1500)
b_1.deposit(100)
b_1.withdrawal(200)


class CurrentAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)

    def withdrawal(self, value):
        if value > 1000:
            print ('Contact your branch manager')
        else:
            super().withdrawal(value)


c_2 = CurrentAccount(1200)
c_2.withdrawal(1200)
c_2.withdrawal(200)


class SavingsAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, value):
        value += 0.05 * value

        super().deposit(value)


s_1 = SavingsAccount(2000)
s_1.deposit(500)
