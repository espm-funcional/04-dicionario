def fibonacci(n, aux={}):    
    if n in aux:
        return aux[n]  

    if n <= 0:
        return 0
    elif n == 1:
        return 1    
    
    aux[n] = fibonacci(n - 1, aux) + fibonacci(n - 2, aux)
    return aux[n]

def main():    
    n = int(input("Digite um número inteiro para calcular o Fibonacci: "))
    
    if n < 0:
        print("O número deve ser maior ou igual a zero.")
    else:
        resultado = fibonacci(n)
        print(f"Fibonacci({n}) = {resultado}")

if __name__ == "__main__":
    main()
