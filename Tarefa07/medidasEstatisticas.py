import random

class MedidasDescritivas:
  def __init__(self, dados):
    if not isinstance(dados, list):
      raise TypeError("Os dados devem ser fornecidos como uma lista.")
    self.dados = dados
  
  def calcular_media(self):
    return sum(self.dados) / len(self.dados)
  
  def calcular_mediana(self):
    dados_ordenados = sorted(self.dados)
    n = len(dados_ordenados)
    
    if n % 2 == 0:
      mediana = (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2
    else:
      mediana = dados_ordenados[n // 2]
    
    return mediana
  
  def calcular_moda(self):
    frequencias = {}
    
    for valor in self.dados:
      frequencias[valor] = frequencias.get(valor, 0) + 1
    
    moda = [valor for valor, frequencia in frequencias.items() if frequencia == max(frequencias.values())]
    return moda
  
  def calcular_valor_maximo(self):
    return max(self.dados)
  
  def calcular_valor_minimo(self):
    return min(self.dados)
  
  def calcular_desvio_padrao(self):
    media = self.calcular_media()
    desvio_quad = sum([(valor - media) ** 2 for valor in self.dados]) / len(self.dados)
    desvio_padrao = desvio_quad ** 0.5
    return desvio_padrao
  
  def calcular_variancia(self):
    desvio_padrao = self.calcular_desvio_padrao()
    variancia = desvio_padrao ** 2
    return variancia
  
  def calcular_amplitude(self):
    return self.calcular_valor_maximo() - self.calcular_valor_minimo()
  
  def calcular_coeficiente_variacao(self):
    desvio_padrao = self.calcular_desvio_padrao()
    media = self.calcular_media()
    coef_variacao = (desvio_padrao / media) * 100
    return coef_variacao
  
  @staticmethod
  def gerar_dados_aleatorios(minimo, maximo, quantidade):
    return [random.randint(minimo, maximo) for _ in range(quantidade)]


# Exemplo de uso
dados = MedidasDescritivas.gerar_dados_aleatorios(1, 100, 10)

try:
  medidas = MedidasDescritivas(dados)
  print(f"Dados: {dados}")
  print(f"Média: {medidas.calcular_media()}")
  print(f"Mediana: {medidas.calcular_mediana()}")
  print(f"Moda: {medidas.calcular_moda()}")
  print(f"Valor máximo: {medidas.calcular_valor_maximo()}")
  print(f"Valor mínimo: {medidas.calcular_valor_minimo()}")
  print(f"Desvio Padrão: {medidas.calcular_desvio_padrao()}")
  print(f"Variância: {medidas.calcular_variancia()}")
  print(f"Amplitude: {medidas.calcular_amplitude()}")
  print(f"Coeficiente de Variação: {medidas.calcular_coeficiente_variacao()}")
except TypeError as e:
  print(f"Erro: {e}")