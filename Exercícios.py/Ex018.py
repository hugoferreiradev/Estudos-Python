# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ân = float(input('Digite o ângulo: '))
seno = sin(radians(ân))
print('O ângulo de {} tem o seno de {:.2f}'.format(ân, seno))
coss = cos(radians(ân))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ân, coss))
tang = tan(radians(ân))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ân, tang))

