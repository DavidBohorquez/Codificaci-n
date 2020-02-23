def count_upper(cad):
    aux = 0
    for x in cad:
        if x.isupper(): aux+=1
    return aux

print("El número de mayúsculas en la cadena de caracteres es:" , count_upper(input("Ingrese una oración:\n")))