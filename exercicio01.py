
# função para agrupar as palavras por tamanho
def agrupar(palavras: list[str]) -> dict[int, list[str]]:
    agrupamento = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in agrupamento:
            agrupamento[tamanho] = []
        agrupamento[tamanho].append(palavra)
    return agrupamento
        

# código da função main()
def main():
    palavras = input('entre com as palavras separadas por espaço: ').split()
    agrupamento = agrupar(palavras)
    
    # impressão dos dados do dicionário
    for tamanho, lista in sorted(agrupamento.items()):
        print(f'tamanho {tamanho}: {lista}')

# chamada da função main()
if __name__ == '__main__':
    main()