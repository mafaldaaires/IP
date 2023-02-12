def f(x):
    return x**3-5*x+2

def bissect(a,b,tol):
    fa = f(a)
    while b-a > tol:
        m = (a+b)/2
        fm = f(m) # temos de definir a função f
        if fm == 0: 
            return m
        if fm*fa > 0:
            a = m 
            fa = fm
        else:
            b=m 
    return (a+b)/2

#NOTA
#Em vez de:
#def bissect(a,b,tol):
#    while b-a > tol:
#        m = (a+b)/2
#        fm = f(m) # temos de definir a função f
#        if fm == 0: 
#            return m
#        if fm*f(a) > 0:
#            a=m 
#        else:
#            b=m 
#    return (a+b)/2
#Neste caso, em cada iteração, calculamos f(a).
#Se definirmos f(a) no inicio do programa, nao precisamos de calcular f(a) em cada iteração
#O programa fica mais eficiente

#NOTA
#def bissect(f,a,b,tol):
#    fa = f(a)
#    while b-a > tol:
#        m = (a+b)/2
#        fm = f(m) # temos de definir a função f
#        if fm == 0: 
#            return m
#        if fm*fa > 0:
#            a = m 
#            fa = fm
#        else:
#            b=m 
#    return (a+b)/2
#Modo de nao termos de criar uma funcao a parte para definir a funcao: Funcao passada a funcao como argumento
#No terminal corremos esta funcao como: 
# >>> bissect(lambda x: x**3-5*x+2,0,1,0.01)