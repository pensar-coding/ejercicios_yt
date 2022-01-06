"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def funcion_max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(funcion_max(-1,-5))


"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def funcion_max_de_tres(n1,n2,n3):
    if n1 > n2 and n1> n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(funcion_max_de_tres(10,-1,2))

"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""
def is_vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

print(is_vocal('e'))


"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def sum(lista):
    result = 0
    for n in lista:
        result = result + (n)
    
    print(result)

def mult(lista):
    result = lista[0]
    i = 1
    while i in range(1,len(lista)):
        result = result * lista[i]
        i +=1
        print(result)

mult([2,2,2])

"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
    return nueva_cadena



inversa('estoy probando')

"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    
print(es_palindromo('arenera'))


"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
def superposicion(lista1,lista2):
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    
    return False
    """
    manera elegante
    for elem in lista1:
        if elem in lista2:
            return True
    
    return False
    """
    
print('Superposicion:')
print(superposicion([1,2,3],[7,4,5]))


"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(caracter,n):
    string = caracter
    print(caracter * n)
    """
    for i in range(1,n):
        string += caracter
    
    print(string)
    """

generar_n_caracteres('abc',1)

"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******
"""
def procedimiento(lista):
    for n in lista:
        histograma = '*' * n
        print(f'{histograma} \n')
    
procedimiento([4,9,7])