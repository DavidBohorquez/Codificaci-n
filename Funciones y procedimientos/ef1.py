def fact(num):
    if(num == 1):
        return num
    else:
        return num*fact(num-1)

print("El factorial del número ingresado es:" , fact(int(input("Ingrese un número: "))))