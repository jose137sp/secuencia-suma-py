def secuencia(n):
    if n == 1 or n == 2 or n == 3:
        return 1

    else: 
        return secuencia(n-1) + secuencia(n-2) + secuencia(n-3)

n= int(input("\nIntroduzca n: "))


print(secuencia(n))