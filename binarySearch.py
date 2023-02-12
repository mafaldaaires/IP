#encontrar valor x na lista v (lista ordenada de forma decrescente)
#retorna a posicao da lista onde esta o valor x
def binarySearch(x,v):
    a = 0
    b = len(v)-1
    while a<=b:
        m = (a+b)//2
        if v[m]==x: return m
        if v[m] < x: b = m-1
        else: a=m+1
    return -1   #nao encontrou o valor x

#Numa lista desordenada, temos de recorrer a pesquisa linear
#Pode requerer n iterações (n=len(v))
def linearSearch(x,v):
    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1