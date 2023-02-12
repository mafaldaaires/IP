class Point:
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.nome=n

    def __str__(self):
        return "(%d,%d)" % (self.x,self.y)

    #Retorna True se tem as mesmas coordenadas
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
        #No terminal: 
        #>>> p1 = Point(0,1,'Joao')
        #>>> p2 = Point(0,1,'Mary')
        #>>> res = p1.__eq__(p2)
        #>>> print(res)

    #retorna True se self e estritamente menor na ordem lexicografica
    def __lt__(self,other):
        return self.nome<other.nome

    #retorna True se self e menor ou igual na ordem lexicografica 
    def __le__(self,other):
        return self.nome<other.nome or self.nome==other.nome
    
    #efetua um deslocamento do ponto de uma posicao na vertical
    def shift_up(self):
        self.y += 1
        return str(self)
    #def scale(self,fator):
    #    #multiplica as coordenadas pelo fator indicado
    #def squareDistance(self,other):
    #    # retorna o quadrado da distancia entre os dois pontos


#class Fraction:
#    def __init__(self, num, denom):
#        if denom == 0:
#            raise ZeroDivisionError("denominador zero")
#        if denom < 0:
#            denom = -denom
#            num = -num
#        d = mdc(abs(num),denom)
#        self.num = num//d
#        self.denom = denom//d
#
#    def __str__(self):
#        # fracao irredutivel com denominador 1 se o valor for inteiro
#        if self.denom == 1:
#            return str(self.num)
#        return "%d/%d" % (self.num, self.denom)
#    
#    def __add__(self,other): # define a operacao +
#        r = Fraction(self.num*other.denom + self.denom*other.num,self.denom*other.denom)
#        return r
#    
#    def __mul__(self, other): # define a operacao *
#        r = Fraction(self.num*other.num, self.denom*other.denom) 
#        return r
#
#
#    def __sub__(self,other): # define a operacao - 
#        sym_other = Fraction(-other.num,other.denom) 
#        return self + sym_other
#
#    def __truediv__(self,other): # define a operacao / 
#        if other.num == 0:
#            raise ZeroDivisionError("Divisao por zero") 
#        return self*Fraction(other.denom,other.num)
#    
#    def __eq__(self,other): # define a operacao == 
#        return self.num*other.denom == self.denom*other.num
#
#    
#    def __lt__(self,other): # define a operacao < 
#        return self.num*other.denom < self.denom*other.num
#
#
#    def __le__(self,other): # define a operacao <= 
#        return self.num*other.denom <= self.denom*other.num
#
#def mdc(a,b):
#    while b!=0:
#        r=a%b
#        a=b
#        b=r
#    return a
#    #Versão 2
#    #if b == 0:
#    #    if a == 0:
#    #        raise ValueError("mdc(%d,%d) indefinido" % (a,b))
#    #    return a
#    #return mdc(b, a%b)
#
##String -> Fracção
#def str2Fraction(s):
#    if '/' in s:
#        numerador,denominador = s.split('/')
#        return Fraction(int(numerador),int(denominador))
#    return Fraction(int(s),1)
#
##Calcula o valor de uma String (soma)
#def calcula(expr):
#    list = expr.split('+')
#    res = str2Fraction(list[0])
#    for i in range(1,len(list)):
#        res = res.__add__(str2Fraction(list[i]))
#    return res
#
#Ta mal
#def isolar(expr):
#    list = expr.split('+')
#    return list
#
#def soma_algebrica(expr):