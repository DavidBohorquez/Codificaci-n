from random import randint

def pirnt_matrix(m):
    for i in range(0,4): 
        for j in range(0,4): 
            print(m[i][j], end = " ") 
        print() 

def sum_matrix():
    a = [[randint(0,9) for i in range(0,4)] for j in range(0,4)]
    pirnt_matrix(a)

    aux = 0
    for i in range(0,4):
        for j in range(0,4):
            if(i < j):
                aux += a[i][j]
    print("La suma de los valores por encima de la diagonal principal es:" , aux)

sum_matrix()

