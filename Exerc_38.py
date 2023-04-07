salario=float(input("digite o salario meu nobre: "))

if salario<=280:
    aumento20=(salario/100*20)+salario
    print(aumento20)
    print('20')
elif 280<salario<=700:
    aumento15=(salario/100*15)+salario
    print(aumento15)
    print('15')
elif 700< salario<=1500:
    aumento10=(salario/100*10)+salario
    print(aumento10)
    print('10')
elif salario>1500:
    aumento5=(salario/100*5)+salario
    print(aumento5)
    print('5')
else:
    print("digite um salario válido")
