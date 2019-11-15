
LP = ['a', 'i', 'o', 'b', 'q', 'c', 'd', 'r', 'f', 'j', 'u', 'k', 'l', 'e', 'w',
     'g', 'x', 'm', 'y', 'n', 'z', 'p', 's', 'h', '1', '2', '3', '4', 't', 'v']

class tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

def inorder(a):
    if a.right == None:
        return a.label
    elif a.label == "-":
        return "-" + inorder(a.right)
    else:
        return "(" + inorder(a.left) + a.label + inorder(a.right) + ")"

def regla():
    x1 = ""
    for q in range(14):
        x1 += inorder(eval("R"+str(q+1)))
        if q < 13:
            x1 += "Y"
    return x1

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
A4 = tree("Y", Ns, Ne)
A5 = tree("Y", Nc, Nf)
A6 = tree("Y", Np, Nh)
A7 = tree("Y", Ng, Ne)
A8 = tree("Y", Nl, A7)

R1 = tree(">", j, A0)
R2 = tree(">", b, A1)
R3 = tree(">", s, A2)
R4 = tree(">", d, A3)
R5 = tree(">", c, A4)
R6 = tree(">", e, A5)
R7 = tree(">", a, A6)
R8 = tree(">", l, Nf)
R9 = tree(">", t, Nd)
R10 = tree(">", g, Nf)
R11 = tree(">", f, A8)
R12 = tree(">", m, Nj)
R13 = tree(">", p, Na)
R14 = tree(">", h, Nb)

print(regla())
