def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i

    else:
        yield []

def bienParentizadas(n):
    lista = []
    for m in misterio(["(" for i in range(n)]+[")" for i in range(n)]):
        a = 0
        c = 0
        agrega = True
        string = ""
        if lista.count(m) == 0:
            for i in m:
                if i == "(":
                    a += 1
                    string += i
                else:
                    c += 1
                    string += i
                if c > a:
                    agrega = False
                    break 
            if agrega:
                lista.append(m)
                yield string

for m in bienParentizadas(4):
    print(m)