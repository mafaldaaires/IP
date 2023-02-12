#Métodos __init__ efetua a inicialização dos objetos
#Métodos __str__ efetua a "impressão" correta dos objetos : em vez do nome da classe e do endereço de memória imprime o que realmente quero 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "Point (%g,%g)" %(self.x,self.y)

class Rectangle:
    def __init__(self,w,h,point):
        self.width=w
        self.height=h
        self.corner=point

    def __str__(self):
        return "Rectangle (%g,%g,%s)" %(self.width,self.height,str(self.corner))