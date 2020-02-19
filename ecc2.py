def sum_range(a,b):
    down = a; up = b
    aux = 0
    if(a > b): down = b; up = a
    for x in range(down,up+1):
        aux+=x
    return aux

print(sum_range(int(input("Ingrese el límite inferior: ")),int(input("Ingrese el límite superior: "))))