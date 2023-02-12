def adivinha(a,b):
    #a=1
    #b=1000
    #  Se definirmos a e b depois de os por como argumentos da funçao, 
    # a e b passam a ter os valores posteriormente definidos.
    print("Pense num inteiro de %d a %d mas não o diga!" %(a,b))
    while a < b:
        m = (a+b)//2
        print("Maior do que %d? (Indique 0 (não) 1 (sim)\n"% m)
        resp = int(input())
        if resp == 1:
            a = m+1 
        else:
            b=m 
    return b