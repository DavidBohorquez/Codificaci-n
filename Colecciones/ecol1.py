def count(cad):
    t_voc = ('a','e','i','o','u')
    t_cons = ('b,','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z')
    
    aux_voc = 0; aux_cons = 0

    for x in cad:
        for i in t_voc:
            if x == i: aux_voc+=1

    for x in cad:
        for i in t_cons:
            if x == i: aux_cons+=1
            
    return [aux_voc,aux_cons]

lista = count(input("Ingrese una palabra: "))
print("Vocales = ", lista[0], "\nConsonantes = ", lista[1])