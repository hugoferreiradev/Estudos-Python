# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$'))
des = preço - (preço*5/100)
print('Seu preço original era de {} e, seu novo preço é, R${:.2f}'.format(preço, des))
