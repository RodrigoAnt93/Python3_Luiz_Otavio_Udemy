from Exerc_35_class import AccountBank
import Exerc_35_func

client = AccountBank(1234, "Rodrigo", 1)

while True:
    print("=-=" * 5, " Banco CDD ", "=-=" * 5)
    print("O que você deseja: \n"
          "1 - Depositar\n"
          "2 - Sacar:\n"
          "3 - Ativar conta\n"
          "4 - Situação da conta\n"
          "5 - Ativar cheque especial\n"
          "6 - Sair")
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        value = float(input("   Digite o valor a ser depositado: R$"))
        print("   ", end="")
        Exerc_35_func.deposit(client, value)
    elif opc == 2:
        value = float(input("   Digite o valor a ser sacado: R$"))
        print("   ", end="")
        Exerc_35_func.draw(client, value)
    elif opc == 3:
        opc = input("   Você deseja ativar sua conta? [S/N] ").strip().upper()[0]
        if opc == 'S':
            print("   ", end="")
            Exerc_35_func.activate_account(client)
        else:
            print("Opção cancelada.")
    elif opc == 4:
        Exerc_35_func.situation_account(client)
    elif opc == 5:
        value = float(input("   Qual o valor do crédito do cheque especial? "))
        Exerc_35_func.activa_limit(client, value)
    else:
        break
    print('')
print("Fim do Programa.")
