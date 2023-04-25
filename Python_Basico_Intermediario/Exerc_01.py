from datetime import date
nome = 'Rodrigo Antonio'
idade = 29
peso = 118.0
altura = 1.82
ano_atual = date.today().year
print(f'''{nome} tem {idade} anos de idade.
Ele pesa {peso} e sua altura é {altura}. Seu IMC é {peso / (altura * altura):.2f}
{nome} nasceu no ano de {ano_atual - idade}''')