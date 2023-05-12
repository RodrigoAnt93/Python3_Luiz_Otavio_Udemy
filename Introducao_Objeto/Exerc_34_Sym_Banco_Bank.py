"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra."""

import Exerc_34_Sym_Banco_Account
import Exerc_34_Sym_Banco_Person


class Bank:
    def __init__(self,
                 bd_agency: list = None,
                 bd_account: list = None,
                 bd_client: list = None):
        self.bd_agency = bd_agency or []
        self.bd_account = bd_account or []
        self.bd_client = bd_client or []

    def __repr__(self):
        return f'{self.bd_agency!r}, {self.bd_account!r}, {self.bd_client!r}'

    def authenticate(self, agency: Exerc_34_Sym_Banco_Account.Account,
                     account: Exerc_34_Sym_Banco_Account.Account,
                     client: Exerc_34_Sym_Banco_Person.Person):
        if client in self.bd_client and account in self.bd_account and agency in self.bd_agency:
            print(f'Conta autenticada com sucesso.')
        else:
            print(f'conta não autenticada.')


if __name__ in '__main__':
    banco = Bank()
    p1 = Exerc_34_Sym_Banco_Person.Client('Rodrigo', 29)
    p1.account = Exerc_34_Sym_Banco_Account.SavingsAccount(1234, 123456)
    banco.bd_client.append(p1)
    banco.bd_account.append(p1.account.num_account)
    banco.bd_agency.append(p1.account.num_agency)
    banco.authenticate(p1.account.num_agency, p1.account.num_account, p1)
