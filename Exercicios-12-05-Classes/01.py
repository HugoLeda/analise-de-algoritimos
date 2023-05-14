class Produto:
  def __init__(self, produto, preco, medida):
    self.produto = produto
    self.preco = preco
    self.medida = medida

class Cliente:
  def __init__(self, nome, cpf):
    self.nome = nome
    self.cpf = cpf

class Compra:
  def __init__(self, cliente):
    self.cliente = cliente
    self.produtos = []
  
  def adicionarProduto(self, produto, quantidade):
    self.produtos.append({"produto": produto, "quantidade": quantidade})
  
  def removerProduto(self, produto):
    for item in self.produtos:
      if item["produto"] == produto:
        self.produtos.remove(item)
        break

  def removerQtdProduto(self, produto, quantidade):
    for item in self.produtos:
      if item["produto"] == produto:
        item["quantidade"] -= quantidade
        if item["quantidade"] <= 0:
          self.produtos.remove(item)
        break

  def atualizarQuantidade(self, produto, quantidade):
    for item in self.produtos:
      if item["produto"] == produto:
        item["quantidade"] = quantidade
        break

  def valorTotal(self):
    valorCompra = 0    
    for item in self.produtos:
      valorCompra += item["produto"].preco * item["quantidade"]
    return valorCompra  
  
  def imprimirNota(self):
    print('=== Nota Fiscal ===')
    print(f'Cliente: {self.cliente.nome}')
    print('---')
    print('Produto                            Quantidade Preço Valor')
    print('------------------------------------------------------------------------------')
    for item in self.produtos:
      produto = item["produto"]
      quantidade = item["quantidade"]
      valor = produto.preco * quantidade
      print(f'{produto.produto:25} {quantidade:12} R$ {produto.preco:7.2f}   R$ {valor:7.2f}')
    print('------------------------------------------------------------------------------')
    print(f'Valor total de compra: R$ {self.valorTotal():.2f}')



amacianteConfort500 = Produto(produto='Amaciante Confort 500ml', preco=14.50, medida='un')    
arrozAene5kg = Produto(produto='Arroz Aene 5kg', preco=23.00, medida='un')    

clienteJoao = Cliente(
  nome='João Hugo Leda',
  cpf='000.000.000-00'
)

compra1 = Compra(
  cliente=clienteJoao
)

compra1.adicionarProduto(amacianteConfort500, 5)
compra1.adicionarProduto(arrozAene5kg, 2)
compra1.imprimirNota()

compra1.removerQtdProduto(amacianteConfort500, 2)
compra1.imprimirNota()