class Produto:
  def __init__(self, produto, preco, medida):
    self.produto, self.preco, self.medida = produto, preco, medida
    
class Cliente:
  def __init__(self, nome, cpf):
    self.nome, self.cpf = nome, cpf   

class Compra:
  def __init__(self, cliente):
    self.cliente = cliente
    self.produtos = []
      
  def adicionarProduto(self, produto, qtd):
    self.produtos.append([produto, qtd])
    
  def valorTotal(self):
    valorCompra = 0    
    for i in self.produtos:
      valorCompra += i[0].preco * i[1]
    
    return valorCompra
  
  def imprimirNOta(self):
    print('Produto, Quantidade, Preço, Valor')
    for i in self.produtos:
      print(f'{i[0].produto}, {i[1]}, R$ {i[0].preco}, R$ {i[0].preco * i[1]}')
    print(f'Valor total de compra R$ {round(self.valorTotal(), 2)}')

amacianteConfort500 = Produto(produto='amacianteConfort500', preco=14.50, medida='un')    
arrozAene5kg = Produto(produto='arrozAene5kg', preco=23.00, medida='un')    

clienteJoao = Cliente(
  nome='JOão Hugo Leda',
  cpf='000.000.000-00'
)

compra1 = Compra(
  cliente=clienteJoao
)

compra1.adicionarProduto(amacianteConfort500, 5)
compra1.adicionarProduto(arrozAene5kg, 2)
compra1.imprimirNOta()