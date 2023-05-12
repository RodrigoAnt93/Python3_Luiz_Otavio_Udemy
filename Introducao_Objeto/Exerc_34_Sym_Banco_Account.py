"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra."""

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account: int, overdraft: list = None, balance: float = 0):
        self._agency = agency
        self._account = account
        self._overdraft = overdraft
        self._balance = balance

    @abstractmethod
    def draw(self, value: float) -> None:
        pass

    def deposit(self, value: float) -> None:
        self._balance += value
        print(f'Você depositou R${value} e seu saldo atual é R${self._balance}')

    @property
    def balance(self):
        return f'Seu saldo atual é R${self._balance}'

    @property
    def num_agency(self):
        return self._agency

    @property
    def num_account(self):
        return self._account

class CurrentAccount(Account):
    def draw(self, value) -> None:
        if self._balance >= value:
            self._balance -= value
            print(f'Saque Autorizado! Você sacou R${value}')
            return
        else:
            if self._overdraft[0]:
                if self._overdraft[1] >= value:
                    self._overdraft[1] -= value
                    print(f'Saque Cheque Especial Autorizado! Você usou seu cheque especial e sacou R${value}')
                    return
        print(f'Você não tem saldo para fazer esse saque.')
        return

    def __repr__(self):
        return f'Agencia: {self._agency!r}, Conta: {self._account}, C.E: {self._overdraft}, Saldo: {self._balance}'


class SavingsAccount(Account):
    def draw(self, value) -> None:
        if self._balance >= value:
            self._balance -= value
            print(f'Saque Autorizado! Você sacou R${value}')
            return
        print(f'Você não tem saldo para fazer esse saque.')
        return

    def __repr__(self):
        return f'Agencia: {self._agency!r}, Conta: {self._account}, Saldo: {self._balance}'


if __name__ == '__main__':
    c1 = CurrentAccount(1234, 12345, [True, 100], 10)
    print(c1)
    c1.draw(10)
    c1.draw(50)
    print(c1.balance)
    c1.deposit(50)
    print(c1.balance)
    print('*' * 20)
    p1 = SavingsAccount(1234, 23456, [False, 0], 100)
    print(p1)
    p1.draw(50)
    p1.draw(100)
    p1.deposit(50)
    p1.draw(100)