from pickle import FALSE


class Pessoa:
  def __init__(self, nome, idade, pai = '', mae = '', raiz = 0):
    self._nome = nome
    self._idade = idade
    self._pai = pai
    self._mae = mae
    self._raiz = raiz
    
  @property 
  def nome(self):
    return self._nome
  
  @property
  def idade(self):
    return self._idade
  
  @property
  def pai(self):
    return self._pai
  
  @property
  def mae(self):
    return self._mae
  
  def setIdade(self, idade):
    self._idade = idade
    
  def imprimirFamilia(self):
    print('Nome: ', self._nome)
    if (self._raiz == 0):
      print('Pai: ', self._pai.nome)
      print('Mãe: ', self._mae.nome)
      
sandra = Pessoa('Sandra', 37, raiz=1)
antonio = Pessoa('Antonio', 42, raiz=1)
joao = Pessoa('João', 19, sandra, antonio)
joao.imprimirFamilia()