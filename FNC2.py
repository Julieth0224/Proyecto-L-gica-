# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC

import copy

LP = ['a', 'i', 'o', 'b', 'q', 'c', 'd', 'r', 'f', 'j', 'u', 'k', 'l', 'e', 'w',
      'g', 'x', 'm', 'y', 'n', 'z', 'p', 's', 'h', '1', '2', '3', '4', 't', 'v']

r1 = "(j>(-bY-m))"
r2 = "(b>(-jY-h))"
r3 = "(s>(dY-c))"
r4 = "(d>(sY-t))"
r5 = "(c>-s)"
r6 = "(e>-f)"
r7 = "(a>(-pY-h))"
r8 = "(l>-f)"
r9 = "(t>-d)"
r10 = "(g>-f)"
r11 = "(f>(-lY-gY-e))"
r12 = "(m>-j)"
r13 = "(p>-a)"
r14 = "(h>(-bY-a)"

class tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

a = tree("a", None, None)
b = tree("b", None, None)
c = tree("c", None, None)
d = tree("d", None, None)
f = tree("f", None, None)
j = tree("j", None, None)
l = tree("l", None, None)
e = tree("e", None, None)
g = tree("g", None, None)
m = tree("m", None, None)
p = tree("p", None, None)
s = tree("s", None, None)
h = tree("h", None, None)
t = tree("t", None, None)

Na = tree("-", None, a)
Nb = tree("-", None, b)
Nc = tree("-", None, c)
Nd = tree("-", None, d)
Nf = tree("-", None, f)
Nj = tree("-", None, j)
Nl = tree("-", None, l)
Ne = tree("-", None, e)
Ng = tree("-", None, g)
Nm = tree("-", None, m)
Np = tree("-", None, p)
Ns = tree("-", None, s)
Nh = tree("-", None, h)
Nt = tree("-", None, t)

A0 = tree("Y", Nb, Nm)
A1 = tree("Y", Nj, Nh)
A2 = tree("Y", d, Nc)
A3 = tree("Y", s, Nt)
A6 = tree("Y", Np, Nh)
A7 = tree("Y", Ng, Ne)
A8 = tree("Y", Nl, A7)
A9 = tree("Y", Nb, Na)

R1 = tree("Y", j, A0)
R2 = tree("Y", b, A1)
R3 = tree("Y", s, A2)
R4 = tree("Y", d, A3)
R5 = tree("Y", c, Ns)
R6 = tree("Y", e, Nf)
R7 = tree("Y", a, A6)
R8 = tree("Y", l, Nf)
R9 = tree("Y", t, Nd)
R10 = tree("Y", g, Nf)
R11 = tree("Y", f, A8)
R12 = tree("Y", m, Nj)
R13 = tree("Y", p, Na)
R14 = tree("Y", h, A9)

def polaca(a):
    p1 = ""
    p1 += a.label
    if a.right != None and a.left != None:
        p1 += polaca(a.left)
        p1 += polaca(a.right)
    elif a.right != None and a.left == None:
        p1 += polaca(a.right)
    return p1

def inversa(a):
    x3 = polaca(a)
    return x3[::-1]

def regla_pi():
    x1 = ""
    for q in range(14):
        x1 += inversa(eval("R"+str(q+1)))
    x1 += 13*"Y"
    return x1

def regla():
    x1 = ""
    for q in range(14):
        x1 += eval("r"+str(q+1))
        if q < 13:
            x1 += "Y"
    return x1

def string2tree(A, LetrasProposicionales):
    conectivos = ["O", "Y", "Y"]
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(tree(c, None, None))
        elif c == "-":
            formulaaux = tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaaux)
        elif c in conectivos:
            formulaaux = tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaaux)
    return pila[-1]

def inorder(a):
    if a.right == None:
        return a.label
    elif a.label == "-":
        return "-" + inorder(a.right)
    else:
        return "(" + inorder(a.left) + a.label + inorder(a.right) + ")"



def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 3000)]
    atomos = letrasProposicionalesA + letrasProposicionalesB
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    l = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if s in atomos and len(pila) > 0 and pila[-1] == '-' :
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(atomo + '=-' + s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = pila[-1]
            o = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            l.append(atomo + "=(" + v + o + w+")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    b = ''
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in l:
        y = enFNC(x)
        b += 'Y' + y
    b = atomo + b

    return b

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    l = []
    while len(C)>0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            l.append(literal)
            C = C[2:]
        else:
            l.append(s)
            C = C[1:]
    return l

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    l = []
    i = 0
    while len(A)> 0:
        if i >= len(A):
            l.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                l.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i+=1
    return l

def clausulaU(S):
    for i in S:
        if(len(i)==1):
            return i[0]
    return '-1'

def neg(a):
    if len(a) == 1:
        l = "-" + a
    else:
        l = a[-1]
    return l


def unitPropagate(S, I):
    bool = True
    while bool:
        for k in S:
            if len(k) == 0:
                #return "Insatisfacible", {}
                break

        cont = 0
        for i in S:
            if len(i) == 1:
                cont += 1
                lit = i[0]
                if len(lit) == 1:
                    pp = lit
                    compl = "-" + lit
                    valor = 1

                elif(len(lit) == 2):
                    pp = lit[1]
                    compl = lit[1]
                    valor = 0

                for j in S:
                    if j != i:
                        if lit in j:
                            S.remove(j)
                I[pp] = valor
                S.remove(i)
                #print(i)


        if cont == 0:
            bool = False
        else:
            for k in S:
                if compl in k:
                    k.remove(compl)
    return S, I

def DPLL(s, i):
    void = []
    s, i = unitPropagate(s,i)
    if void in s:
        return "Insatisfacible", {}
    elif len(s) == 0:
        return "Satisfacible", i
    l = ""
    for y in s:
        for x in y:
            if x not in i.keys():
                l = x
    l_comp = neg(l)
    if l == "":
        return None
    Sp = copy.deepcopy(s)
    Sp = [n for n in Sp if l not in n]
    for q in Sp:
        if l_comp in q:
            q.remove(neg(l))
    Ip = copy.deepcopy(i)
    if l[0] == "-":
        Ip[l[1]] = 0
    else:
        Ip[l] = 1
    S1, I1 = DPLL(Sp, Ip)
    if S1 == "Satisfacible":
        return S1, I1
    else:
        Spp = copy.deepcopy(s)
        Spp = [q for q in Spp if neg(l) not in q]
        for h in Spp:
            if l in h:
                h.remove(l)
        Ipp = copy.deepcopy(i)
        if l[0] == "-":
            Ipp[l[1]] = 0
        else:
            Ipp[l] = 1
        return DPLL(Spp, Ipp)


i = {}
F = regla_pi()
reg = regla()
T = string2tree(F, LP)
Regla = inorder(T)
TS = Tseitin(Regla, LP)
Clau = formaClausal(TS)
S, U = DPLL(Clau,i)
interpretaciones = {}
for l in U.keys():
    if l in LP:
        interpretaciones[l] = U[l]

print(interpretaciones)
