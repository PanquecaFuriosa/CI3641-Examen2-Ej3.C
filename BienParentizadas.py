def ins(e, ls):
    """Función que determina todas las maneras de insertar un elemento en una lista

    Args:
        e (any): Elemento cualquiera a ser insertado.
        ls (list): Lista a la cual se le insertará e.

    Yields:
        lis: Lista con el elemento insertado en alguna posición.
    """
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    """Función que determina las posibles permutaciones de los elementos
    de un arreglo.

    Args:
        ls (list): Lista a determinar las posibles permutaciones.

    Yields:
        list: Lista con una permutación.
    """
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i

    else:
        yield []

def bienParentizadas(n):
    """Función que determina las posibles combinaciones
    de un número n de paréntesis, de manera válida.

    Args:
        n (int): Número de pares de paréntesis a permutar.

    Yields:
        str: Una permutación bien patentizada.
    """
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