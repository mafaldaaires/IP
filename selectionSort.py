#Ordenar uma lista v por ordem decrescente
#[7, 8, 56, 45, 32, 54, 76, 56, 43, 2, 3, 4]
                   # |
                   # V
#[76, 56, 56, 54, 45, 43, 32, 8, 7, 4, 3, 2]

#i é o indice atual na lista v
def posmax(i,v):
    pmax = i
    for i in range(i+1,len(v)):
        if (v[i]>v[pmax]):
            pmax = i
    return pmax

def selection_sort(v):
    #Percorre a lista ate a penultima posicao
    for i in range(len(v)-1):
        x = posmax(i,v)
        #i é a posicao atual
        #Se x=i+1 (x e a posicao maxima) => posicao maxima é a ultima
        #Trocar o ultimo pelo penultimo, caso a posicao maxima seja a ultima
        if (x!=i):
            aux = v[x]
            v[x] = v[i]
            v[i] = aux