import binario as bi

x , y = input("Ingrese dos números binario con espacio: ").split()

print("Suma:",format(bi.sum(x,y),"0b"),"\nResta:",format(bi.min(x,y),"0b"),"\nMultiplicación:",format(bi.mult(x,y),"0b"),
    "\nDivisión:",format(bi.div(x,y),"0b"))
