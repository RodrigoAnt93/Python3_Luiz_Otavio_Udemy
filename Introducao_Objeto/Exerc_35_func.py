from Exerc_35_class import AccountBank


def deposit(obj: AccountBank, value: float):
    obj.deposit(value)
    return print(f"R${value} foi depositado na conta.")


def draw(obj: AccountBank, value: float):
    result = obj.draw(value)
    if result == 1:
        return print(f"Saque Autorizado. Valor de R${value} será sacado.")
    else:
        print("Saque não autorizado.")


def activate_account(obj: AccountBank):
    result = obj.activate_account()
    if result == 1:
        print("A conta foi ativada.")
    else:
        print("Conta já ativa.")


def situation_account(obj: AccountBank):
    result = obj.situation_account()
    print(f'    O status da conta é {result[0]}')
    print(f'    O saldo é R${result[1]}')
    if result[2]:
        print(f"    Seu cheque especial é R${result[3]}")
        print(f"    Seu saldo do cheque especial é R${result[4]}")


def activa_limit(obj: AccountBank, value):
    result = obj.limit_(value)
    if result == 1:
        print("   Seu Cheque Especial foi autorizado.")
    else:
        print("   Não foi possível autorizar o cheque especial.")
