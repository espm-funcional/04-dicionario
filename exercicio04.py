def calcular_frequencia_letras(frase):    
    frequencia = {}  

    for letra in frase:
        if letra.isalpha():  
            letra = letra.lower()  
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1

    return frequencia

def main():    
    frase = input("Digite uma frase: ")
    
    frequencias = calcular_frequencia_letras(frase)
    
    print("\nFrequência das letras:")
    for letra, contagem in sorted(frequencias.items()):  
        print(f"{letra}: {contagem}")

if __name__ == "__main__":
    main()
