# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km = float(input('Quantos km foram percorridos durante o aluguel do veículo? '))
da = int(input('Por quantos dias o veículo foi alugado? '))

r = km*0.15
diaria = da*60
t = r+diaria

print('O carro foi alugado por {} dias, portanto, o valor a ser pago pelos dias do aluguel é de R${:.2f}\nE os km percorridos foram {}km/h, portanto, o valor a ser pago é de R${:.2f}, valor cobrado por km percorridos.\nE o total a ser pago é de R${:.2f}.'.format(da, diaria, km, r, t))