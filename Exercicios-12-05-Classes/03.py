from datetime import datetime

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


class Livro:
  def __init__(self, nome, autor, genero):
    self.nome = nome
    self.autor = autor
    self.genero = genero

  def get_nome(self):
    return self.nome

  def get_autor(self):
    return self.autor

  def get_genero(self):
    return self.genero


class Emprestimo:
  emprestimos_ids = set()

  def __init__(self, id, pessoa, livro, data):
    if id in Emprestimo.emprestimos_ids:
      raise ValueError("ID de empréstimo já existe.")
    self.id = id
    self.pessoa = pessoa
    self.livro = livro
    self.data = datetime.strptime(data, "%d-%m-%Y").date()
    Emprestimo.emprestimos_ids.add(id)

  def imprimirEmprestimo(self):
    data_formatada = self.data.strftime("%d/%m/%Y")
    print(f'Em {data_formatada}, {self.pessoa.get_nome()} emprestou o livro {self.livro.get_nome()}')


joao = Pessoa('João', '000.000.000-00', '16-08-2003')
oPequenoPrincipe = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupery', 'Literatura infantil')

try:
  emprestimo1 = Emprestimo(1, joao, oPequenoPrincipe, '14-05-2023')  
except ValueError as e:
  print(f"Erro ao criar empréstimo: {str(e)}")

emprestimo1.imprimirEmprestimo()