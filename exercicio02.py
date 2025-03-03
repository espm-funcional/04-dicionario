def tem_palavras_repetidas(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def main():
    
    entrada = input("Digite uma lista de palavras separadas por espaço: ")
        
    palavras = entrada.split()
    
    resultado = tem_palavras_repetidas(palavras)
    
    if resultado:
        print("A lista contém palavras repetidas.")
    else:
        print("A lista não contém palavras repetidas.")

if __name__ == "__main__":
    main()
