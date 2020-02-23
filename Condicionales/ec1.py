def orden(cad):
    if (cad[0]<cad[1] and cad[1]<cad[2]):
        return True
    else:
        return False

def main():
    cad = [int(input("Ingrese num1: ")), int(input("Ingrese num2: ")), int(input("Ingrese num3: "))]
    
    if(orden(cad)):
        print("Los tres número han sido introducidos en orden creciente")
    else:
        print("Los tres número no han sido introducidos en orden creciente")

main()
    

