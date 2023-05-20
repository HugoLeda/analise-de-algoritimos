class Pessoa:
  def __init__(self, nome, cpf, dataNascimento):
    self._nome = nome
    self._cpf = cpf
    self._dataNascimento = dataNascimento

  @property
  def nome(self):
    return self._nome

  @property
  def cpf(self):
    return self._cpf

  @property
  def data_nascimento(self):
    return self._dataNascimento
  
  def alterar_nome(self, nome):
    self._nome = nome
  
class ContaCorrente:
  def __init__(self, correntista, saldo=0):
    self._correntista = correntista
    self._saldo = saldo
    self._depositos = []
    self._saques = []
  
  def depositar(self, valor):
    self._depositos.append(valor)
    self._saldo += valor
  
  def sacar(self, valor):
    if self._saldo >= valor:
      self._saques.append(valor)
      self._saldo -= valor
    else:
      raise ValueError('Valor indisponível')
    
  @property
  def saldo(self):
    return self._saldo

  def alterar_nome_correntista(self, nome):
    self._correntista.alterar_nome(nome)
  
  @property
  def nome_correntista(self):
    return self._correntista.nome


joao = Pessoa('João', '487.249.608-61', '16-08-2003')
conta1 = ContaCorrente(joao)
conta1.depositar(500)
conta1.sacar(200)
print(conta1.saldo)
conta1.alterar_nome_correntista('João Hugo')
print(conta1.nome_correntista)
