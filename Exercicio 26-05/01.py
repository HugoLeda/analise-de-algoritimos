class Bichinho:
  def __init__(self, nome, fome, saude, idade):
    if not isinstance(fome, int):
      raise TypeError("Os dados devem ser fornecidos como um valor inteiro.")
    if not isinstance(saude, int):
      raise TypeError("Os dados devem ser fornecidos como um valor inteiro.")
    if not isinstance(idade, int):
      raise TypeError("Os dados devem ser fornecidos como um valor inteiro.")
    self._nome = nome
    self._fome = fome
    self._saude = saude
    self._idade = idade
    
  @property 
  def nome(self):
    return self._nome
  
  @property
  def fome(self):
    return self._fome
  
  @property
  def saude(self):
    return self._idade
  
  @property
  def idade(self):
    return self._idade
  
  def setNome(self, nome):
    self._nome = nome
    
  def setIdade(self, idade):
    self._idade = idade
    
  def setFome(self, fome):
    self._nome = fome
  
  def setSaude(self, saude):
    self._saude = saude
    
  def alimentar(self):
    if (self._fome < 100):
      self._fome += 1
      self._saude += 1   
  
  def getHumor(self):
    media = (self._fome + (self._saude * 2)) / 3
    if (self._idade < 3):
      media = media * 1.3
    if (media < 3):
      humor = 'muito triste'
    elif (media < 5):
      humor = 'triste'
    elif (media < 7):
      humor = 'feliz'
    else:
      humor = 'muito feliz'

    return humor
  
violeta = Bichinho('Violeta', 100, 100, 2)
violeta.alimentar()
print('Nome do bichinho: ', violeta.nome)
print('Idade: ', violeta.idade)
print('Humor: ', violeta.getHumor())