import time

while True:  
    h,m,s = map(int,input("Ingrese un timepo en horas, minutos y segundos: ").split())
    if((h>-1 and h<25) and (m>-1 and m<61) and ((s>-1 and s<61))):  
        break
    else: print("Tiempo no válido.")

aux_h, aux_m, aux_s = 0,0,0

while True:
    print(aux_h,":",aux_m,":",aux_s)
    if(aux_h==h and aux_m==m and aux_s==s):
        print("End time!!!")
        break
    else:    
        if(aux_s==60):
            aux_s=0
            aux_m+=1
        else:
            aux_s+=1
        if(aux_m==60):
            aux_m=0
            aux_h+=1
    
    time.sleep(1)




