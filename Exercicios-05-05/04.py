def imprimirVerticalEscada(palavra):
    for i in range(len(palavra), 0, -1):
        print(palavra[0:i])
        
imprimirVerticalEscada('João')  