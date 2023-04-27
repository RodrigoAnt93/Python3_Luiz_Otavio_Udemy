#Crie uma classe chamada Conta com as propriedades saldo e titular.
#Em seguida, crie métodos depositar e sacar que alterem o valor do saldo.
#Crie um objeto Conta e teste seus métodos.

class Account:
    def __init__(self):
        self.owner = 'owner'
        self.balance = 0
        self.statement = []

    def deposit(self):
        value = float(input('Valor à depositar: '))
        self.balance += value
        self.statement.append({'deposito': value})
        return 'Deposito realizado com sucesso.'

    def withdraw(self):
        if self.balance > 0:
            value = float(input('Valor à sacar: '))
            if value <= self.balance:

                self.balance -= value
                self.statement.insert(0, {'saque': value})
                return 'Saque Autorizado'
            else:
                return 'Você não tem esse valor em conta.'
        else:
            return 'Você não tem saldo.'

clint = Account()
print('*' * 10, ' BANCO PYTHON ', '*' * 10)
while True:
    print('1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Saldo')
    while True:
        opt = int(input('\nDigite a opção: '))
        if opt in (1, 2, 3, 4):
            break
        else:
            print('Digite uma opção válida.')
            print()
    command = {
        1: lambda: clint.deposit(),
        2: lambda: clint.withdraw(),
        3: lambda: clint.statement if len(clint.statement) > 0 else 'Você não tem transação.',
        4: lambda: f'Saldo em conta é R${clint.balance}' if clint.balance > 0 else 'Conta zerada.'
    }
    command = command.get(opt)
    print(command())
    print()