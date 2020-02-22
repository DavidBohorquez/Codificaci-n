def fibo(n):
    if((n == 0) | (n == 1)):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print("El término de la serie de fibonacci es: " , fibo(int(input("Ingrese el término de la serie de Fibonacci que desea visualizar: "))))