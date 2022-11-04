# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex.: Digite um número: 6.127. O número 6127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um número Real: '))
print('O número real digitado foi {}.\nE a porção inteira  desse número é {}.'.format(num, trunc(num))) # Possibilidade de utilizar a biblioteca floor.

# outra forma de resolução, sem importar bibliotecas.

num = float(input('Digite um número Real: '))
print('O número real digitado foi {}.\nE a porção inteira  desse número é {}.'.format(num, int(num)))