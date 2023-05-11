from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account: int, overdraft: list = None, balance: int = 0):
        self._agency = agency
        self._account = account
        self._overdraft = overdraft
        self._balance = balance

    @abstractmethod
    def draw(self, value) -> None:
        pass

    def deposit(self, value) -> None:
        self._balance += value
        print(f'Seu saldo atual é {self._balance}')

    @property
    def balance(self):
        return self._balance


class CurrentAccount(Account):
    def draw(self, value) -> None:
        if self._balance >= value:
            self._balance -= value
            print(f'Saque Autorizado! Você sacou {value}')
        else:
            if self._overdraft[0]:
                if self