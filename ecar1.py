def delete(cad):
    #cad1 = cad.replace(" ","")
    return cad.replace(" ","")

cad = input("Ingrese una oración:\n")
cad_del = delete(cad)
print("La cadena de caracteres original es:\n" + cad, "\nLa cadena de caracteres sin espacios es:\n" + cad_del)

