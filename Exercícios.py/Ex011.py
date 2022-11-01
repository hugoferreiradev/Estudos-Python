# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta  necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

alt = float(input('Digite qual a altura da parede em metros: '))
lar = float(input('Digite a largura de uma parede em metros: '))
a = lar*alt

print(f'A parede tem a dimensão de {alt}x{lar} e sua área é de {a}m2')
tinta = a / 2
print(f'Para pintar a parede você precisará de {tinta}l de tinta')