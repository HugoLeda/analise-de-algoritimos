# Escreva um algoritmo que leia dois valores numéricos e depois mostre a diferença entre eles (o primeiro menos o segundo). 

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

diferenca = n1 - n2

print(f'{n1} - {n2} = {round(diferenca, 2)}')