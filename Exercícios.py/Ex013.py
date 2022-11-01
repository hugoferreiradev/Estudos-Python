# Faça um algoritmo que leia o salário e o aumento de 15%

sal = float(input('Qual seu salário? '))
aum = sal + (sal*15/100)
print('O salário sem aumento é de R${:.2f}, e o novo com aumento é de R${:.2f}'.format(sal, aum))