def insert_sort(v):
    for i in range(len(v)):
        x = v[i]
        j = i-1
        #Percorrer a lista da esq para a direita
        while(j>=0 and x > v[j]):
            v[j+1]=v[j]
            j-=1
        v[j+1]=x

# Inicialmente a posicao j+1 é a posicao i.
# Ao percorrer a lista da esq para a direita, enquanto v[i]>v[j] e j diminui,
# v[j+1]=v[j], ou seja, a posicao j+1 fica preenchida com v[j] (posição à esquerda) e v[j] e v[j+1] tem o mesmo valor.
# Na proxima iteração, como j diminui, j+1 vai ser o j da iteração anterior.
# Quando v[i]<=v[j], v[j+1]=v[i].