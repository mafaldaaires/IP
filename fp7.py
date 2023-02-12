def ler_dados(ficheiro):
    try:
        file = open(ficheiro, "r") 
        #cria uma variavel (file) que e uma "copia" do ficheiro para poder manipular NO PYTHON
        #nao podemos manipular no ficheiro original EM PYTHON
        disc = ler_disciplinas(file)
        alunos = ler_dados_alunos(file)
        file.close()
        return (disc,alunos)
    except IOError:
        raise IOError("ficheiro inexistente")
    
def ler_disciplinas(file):
    ndisc = int(file.readline())
    disciplinas = [('None',0)]
    for i in range(ndisc): # disciplina[i] fica associada ao codigo i
        nome = str(file.readline())
        ano = int(file.readline())
        disciplinas.append((nome[:len(nome)-1],ano))
    return disciplinas

def ler_dados_alunos(file):
    alunos = {}
    nalunos = int(file.readline())
    for i in range(nalunos):
        nome = str(file.readline())
        linha = list(map(int,file.readline().split()))
        alunos[linha[0]] = (nome[:len(nome)-1],linha[1],linha[2:])
    return alunos

def anoAluno(codigo):
    ano = codigo//1000000
    return ano

def cursoAluno(codigo):
    curso = (codigo%1000000)//1000
    return curso

#auxiliar p/discAluno
def nomeAluno(codigo,alunos):
    return alunos[codigo][0]

#falta o 7)
def discAluno(codigo,alunos,disciplinas,ficheiro):
    try:
        f = open(ficheiro,"w")
        f.write("Disciplinas de %d (%s)"%(codigo,nomeAluno(codigo,alunos)))
        for i in (alunos[codigo][2]):
            f.write("%s" % (disciplinas[i][0]))
        #f = open(ficheiro,"r")
        #txt = f.read()
        #return txt
        f.close()
    except KeyError:
        f.close()
        raise KeyError("codigo inexistente")

def discAno(ano,disciplinas):
    list = []
    for i in range (1,len(disciplinas)):
        if disciplinas[i][1]==ano:
            list.append(i)
    return list

def alunos_em_disc(disc,alunos):
    if type(disc)!=int or disc<1:
        raise ValueError("Erro de tipos")
    lista=[]
    for i in (alunos):
        list = alunos[i][2]
        for j in range(len(list)):
            if list[j]==disc:
                lista.append(i)
    return lista

def codigoAluno(nome,alunos):
    list=[]
    for i in alunos:
        if (alunos[i][0]==nome):list.append(i)
    return list

#auxiliar para inscritos_dic
#nome = nome da disciplina
def codigo_disc(nome,disciplinas):
    for i in range(1,len(disciplinas)):
        if (disciplinas[i][0]==nome): 
            return i
    return 0  #retorna 0 se o nome da disciplina nao existe

def inscritos_disc(nome,disciplinas,alunos):
    disc = codigo_disc(nome,disciplinas)
    if (disc==0): raise ValueError("disciplina nao existe")
    return alunos_em_disc(disc,alunos)

def media_ndisc(curso,disciplinas,alunos):
    soma_disc=0  #no curso
    n_alunos=0
    for codigo in alunos:
        if (cursoAluno(codigo)==curso):
            soma_disc += alunos[codigo][1]
            n_alunos += 1
    if (n_alunos!=0):
        return soma_disc//n_alunos
    return 0


def totais_por_disciplina(disciplinas,alunos,ficheiro):
    file = open(ficheiro,"w")
    file.write("Numero de alunos inscritos\n")
    contadores = len(disciplinas)*[0]
    for i in alunos:
        for j in alunos[i][2]:
            contadores[j] += 1
    for d in range(len(disciplinas)):
        file.write("%s: %d\n" %(disciplinas[d][0],contadores[d]))
    file.close()
    
    #porque nao da assim??
    #file = open(ficheiro,"w")
    #file.write("Numero de alunos inscritos\n")
    #for i in range(len(disciplinas)):
    #    sum = 0
    #    list = inscritos_disc(disciplinas[i][0],disciplinas,alunos)
    #    for j in range(len(list)):
    #        sum += 1
    #    file.write("%s: %d\n" %(disciplinas[i][0],sum))
    #file.close()