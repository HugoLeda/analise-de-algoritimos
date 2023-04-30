#Escreva um algoritmo que utilize os operadores aritméticos: adição, subtração, multiplicação, divisão e potenciação entre alguns números.  

# Mostre essas operações.  
import random

def operacao(valor1, valor2, operacao):
  if (operacao == 1):
    resultado =  valor1 + valor2 
    return(f'{valor1} + {valor2} = {resultado}')
  elif (operacao == 2):
    resultado =  valor1 - valor2
    return(f'{valor1} - {valor2} = {resultado}')
  elif (operacao == 3):
    resultado =  valor1 * valor2
    return(f'{valor1} * {valor2} = {resultado}')
  elif (operacao == 4):
    resultado =  valor1 / valor2
    return(f'{valor1} / {valor2} = {resultado}')
  elif (operacao == 5):
    resultado =  valor1 ** valor2
    return(f'{valor1} ^ {valor2} = {resultado}')
  else:
    return 'operação inválida'
  
for i in range(2):
  for j in range (5):
    print(operacao(random.randint(-10000,1000), random.randint(-10000,10000), j+1))
