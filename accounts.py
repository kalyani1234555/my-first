import datetime
import pytz


class Account:
    """ simple account class with balance """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for" + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((self._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} local time was {}".format(amount, trans_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account('Tim', 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()
    tim.withdraw(2000)
    tim.show_transaction()

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
