class Agenda:
  def __init__(self, nome):
    self.nome = nome
    self.contatos = []
    
  def adicionarContato(self, contato):
    self.contatos.append(contato)
  
  def listar(self):
    print(self.nome)
    for i in self.contatos:      
      print(i.nome, i.telefone)
  
class Contato:
  def __init__(self, nome, telefone):
    self.nome, self.telefone = nome, telefone
    
joao = Contato('João', '(11) 1111-1111')
jose = Contato('José', '(22) 2222-2222')
mara = Contato('Mara', '(33) 3333-3333')

minhaAgenda = Agenda('Minha agenda')
minhaAgenda.adicionarContato(joao)
minhaAgenda.adicionarContato(jose)
minhaAgenda.adicionarContato(mara)

minhaAgenda.listar()
