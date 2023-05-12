"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra."""

import Exerc_34_Sym_Banco_Account


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account = None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._name}, {self._age})'
        return f'{class_name}{attrs}'


if __name__ == "__main__":
    c1 = Client('Rodrigo', 29)
    c1.account = Exerc_34_Sym_Banco_Account.CurrentAccount(1234, 123456, [True, 30], 10)
    c1.account.draw(20)
    c1.account.deposit(100)
    c1.account.draw(50)