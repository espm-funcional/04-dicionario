def tem_palavras_repetidas(lista):    
    contador = {}  

    for palavra in lista:
        if palavra in contador:
            return True  
        contador[palavra] = 1
    return False  

def main():   
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
    palavras = entrada.split()  

    if tem_palavras_repetidas(palavras):
        print("A lista contém palavras repetidas.")
    else:
        print("A lista não contém palavras repetidas.")

if __name__ == "__main__":
    main()
