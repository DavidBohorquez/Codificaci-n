import arithmetic as ar

x , y = map(int, input("Ingrese dos número: ").split())

print("Suma:",ar.sum(x,y),"\nResta:",ar.min(x,y),"\nMultiplicación:",ar.mul(x,y),
    "\nDivisión:",ar.div(x,y),"\nPotencia:",ar.pot(x,y))

