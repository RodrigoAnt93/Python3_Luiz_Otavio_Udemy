from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_balance, overdraft: list, agency, account):
        self.account_balance = account_balance
        self.overdraft = overdraft
        self.agency = agency
        self.account = account

    def __repr__(self):
        return

    @abstractmethod
    def draw(self, value) -> int:
        pass

    def extract(self):
        for movement in self.extract:
            print(f'{movement[0]}: R${movement[1]} ')

    def deposit(self, value):
        self.account_balance += value
        return


class CheckingAccount(Account):
    def draw(self, value) -> int:
        if self.account_balance >= value:
            self.account_balance -= value
            return 1
        else:
            if self.overdraft[0]:
                if self.overdraft[1] >= value:
                    self.overdraft[1] -= value
                    return 2
            else:
                return 0


class SavingAccount(Account):
    def draw(self, value) -> int:
        if self.account_balance >= value:
            self.account_balance -= value
            return 1
        else:
            return 0


class Person(ABC):
    def __init__(self, name, birth, obj_account):
        self.name = name
        self.birth = birth
        self.obj_account = obj_account

    @abstractmethod
    def update_address(self, new_address):
        pass


class Client(Person):
    def update_address(self, new_address):
        if isinstance(new_address, dict):
            self.address = new_address






if __name__ == '__main__':
