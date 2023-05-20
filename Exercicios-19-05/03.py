class Calculadora:
  def __init__(self, nome):
    self.nome = nome
  
  def somar(self, valores):
    return sum(valores)
  
  def subtrair(self, v1, v2):
    return v1 - v2
  
  def multiplicar(self, valores):
    produto = 1  # Inicializar o produto como 1
    
    for i in valores:
      produto *= i
    
    return produto
  
  def dividir(self, divisor, dividendo):
    if dividendo == 0:
      return 'Nunca dividirás por ZERO'
    else:
      return divisor / dividendo
    
calc1 = Calculadora('Calc1')
print(calc1.somar([2, 7, 10]))
print(calc1.subtrair(50, 9))
print(calc1.multiplicar([3, 2, 5]))
print(calc1.dividir(10, 5))
