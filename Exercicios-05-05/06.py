carros = []
for i in range(5):
    modelo = input('Digite o nome do modelo do carro: ')
    kmL = float(input('Digite quantos KM em média esse carro faz por litro: '))
    qtd1000Km = 1000 / kmL
    custo1000Km = qtd1000Km * 5.85
    carros.append([modelo, kmL, qtd1000Km])

#a
carrosOrdenada = []    
menor = carros[0]
for i in range(len(carros)):
    print(carros[i][1])
    if (carros[i][1] > menor[1]):
        menor = carros[i]
print(f'Modelo mais economico: {menor[0]}, Km/L: {menor[1]}')
        
#b
for i in carros:
    print(i)