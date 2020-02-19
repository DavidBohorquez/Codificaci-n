def par(a):
    if a == 0:
        return "par."
    elif a < 0:
        return "impar."
    else:
        return par(a-2)

print("El número ingresado es ", par(int(input("Ingrese un número: "))))
