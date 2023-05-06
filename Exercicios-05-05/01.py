# comparar strings]

def comparaString(p1, p2):
    print(p1, len(p1))
    print(p2, len(p2))
    
    if p1 == p2:
        print('as strings possuem conteúdos iguais')
    else:
        print('as strings possuem conteúdos diferentes')
        
    if len(p1) == len(p2):
        print('as strings possuem tamanhos iguais')
    else:
        print('as strings possuem tamanhos diferentes')    

comparaString('Joao', 'Joao')    
comparaString('Joao', 'Jose')