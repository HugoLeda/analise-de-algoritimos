   
    
def computarSaltos():
    atletas = []
    nome = 'a'
    while (nome != '' or nome != ' '):        
        nome = input('Digite o nome do atleta: ')
        if (nome == '' or nome == ' '):
            print(atletas)
            return
        saltos = [0] * 5
        for i in range (5):
            saltos[i] = float(input('Digite a distância do salto: '))
            
        media = sum(saltos) / 5
        atletas.append([nome, saltos, media])
    for i in atletas:
        print(i)


computarSaltos()
