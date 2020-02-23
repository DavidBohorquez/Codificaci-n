def dig(num):
    if(num==0):
        return 0
    else:
        return 1 + dig(num//10)

print("El número de dígitos del número es:", dig(int(input('Ingrese un número: '))))