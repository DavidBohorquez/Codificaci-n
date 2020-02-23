def sum(a,b):
    return a+b

def min(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def pot(a,b):
    if(b==0):
        return 1
    else:
        return a * pot(a,b-1)
