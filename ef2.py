def check(c):
    print(ord(c))
    if(ord(c)>47 and ord(c)<58):
        return "es un dígito."
    else:
        return "no es un dígito."

print("El caracter ingresado," , check((input("Ingrese un caracter: "))))