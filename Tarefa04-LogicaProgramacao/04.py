# O sistema de avaliação de determinada disciplina é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. 

# Elabore um algoritmo que calcule a média final de um aluno desta disciplina. 
import random

def media(n1, n2, n3):
  resultado = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
  return resultado

for i in range (5): 
  n1 = random.randint(0,10)
  n2 = random.randint(0,10)
  n3 = random.randint(0,10)
  mediafinal = media(n1, n2, n3)
  print(f'Aluno {i}: \nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\nmédia: {mediafinal}\n\n')