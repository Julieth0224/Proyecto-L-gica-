
letras = ['p', 'q', 'r', 's']
alv = ['p', 'q', 'r', 's', '~p', '~q', '~r', '~s']
neg = ['~p', '~q', '~r', '~s']
Conectores = ['v', '&', '-', '*']

class Tree():
    def __init__(self, l, iz, der):
        self.label = l
        self.left = iz
        self.right = der


def parCom(a):
    for q in a:
        for d in a:
            if d==("~"+q):
                return True
    return False

def literal(a):
    x = 0
    for q in a:
        for f in alv:
            if q==f:
                x += 1
    if x == len(a):
        return True
    else:
        return False

def hayLiteral(a):
    for q in a:
        for n in q:
            if n not in alv:
                return "Hay una formula que no es un literal"
    return "Todas son literales"    


def algoritmo(t):
    while len(t)!=0:
        for h in t:
            if literal(h)==True:
                if parCom(h)==True:
                    print(h, "cerrada")
                    t.remove(h)
                else:
                    print(h, "abierta")
                    t.remove(h)
            else:
                for q in h:
                    if literal(q)==False:
                        print(q)
                t.remove(h)
    if len(t)==0:
        print("End")

def interpsTrue(h):
    lista = []
    for q in h:
        if literal(q)==True:
            if parCom(q)==False:
                lista.append(q)
    return lista
            
def reglas(a):
    if a.label == "~":
        h = a.right
        if a.right in neg:
            return "1a"
        elif h.label in Conectores:
            if h.label == "&":
                return "1b"
            elif h.label == "v":
                return "3a"
            elif h.label == "-":
                return "4a"
    elif a.label in Conectores:
        if a.label == "&":
            return "2a"
        elif a.label == "v":
            return "2b"
        elif a.label == "-":
            return "3b"
        

lista = ["p", "q", "~p", "~q"]
lista1 = ['~(p&q)']
lista2 = [['p', '~p'],['p', 'q'], ['~p', 'q'], ['p', '~~q'], ['~~p', '~(p&q)']]
lista3 = [['p'], ['~~p', 'q'], ['q', '~q'], ['~(p&~q)', 'q']]
lista4 = [['p', 'q'], ['q', '~q'], ['q']]

P = Tree('p', None, None)
Q = Tree('q', None, None)
R = Tree('r', None, None)
S = Tree('s', None, None)
Np = Tree('~', None, P)
Nq = Tree('~', None, Q)
Nr = Tree('~', None, R)
Ns = Tree('~', None, S)
A0 = Tree()

algoritmo(lista3)
print(interpsTrue(lista4))
