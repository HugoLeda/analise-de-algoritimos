class Pessoa:
  def __init__(self, nome, cpf, dataNascimento):
    self.nome = nome
    self.cpf = cpf
    self.dataNascimento = dataNascimento

  def get_nome(self):
    return self.nome

  def get_cpf(self):
    return self.cpf

  def get_dataNascimento(self):
    return self.dataNascimento
  
  def alterarNome(self, nome):
    self.nome = nome
  
class contaCorrente:
  def __init__(self, correntista, saldo = 0):
    self.correntista = correntista
    self.saldo, self.depositos, self.saques = saldo, [], []
  
  def depositar(self, valor):
    self.depositos.append(valor)
    self.saldo += valor
  
  def sacar(self, valor)  :
    self.saques.append(valor)
    
    if self.saldo >= valor:
      self.saldo -= valor
    else:
      print('Valor indisponivel')
    
  def get_saldo(self):
    return self.saldo

  def alterarNome(self, nome):
    self.correntista.alterarNome(nome)
  
  def get_nomeCorrentista(self):
    return self.correntista.nome

joao = Pessoa('João', '487.249.608-61', '16-08-2003')   
conta1 = contaCorrente(joao)
conta1.depositar(500)
conta1.sacar(200)
print(conta1.get_saldo())
conta1.alterarNome('João Hugo')
print(conta1.get_nomeCorrentista())