# coding=utf-8
# __Author__="Javier Vinal Costa"

import  random

# Función que determina si un número es par.
def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Función que determina si un número es impar.
def esImpar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False

def generarPares(valores, inicio):
    pares = []
    numero = inicio

    if esImpar(inicio):
        numero = inicio + 1

    for i in range(valores):
        pares.append(numero)
        numero += 2

    return pares

def generarImpares(valores, inicio):
    impares = []
    numero = inicio

    if esPar(inicio):
        numero = inicio + 1

    for i in range(valores):
        impares.append(numero)
        numero += 2

    return impares

# Programa principal
def main():
    print("Par e impar")
    n = int(input("Introduzca un número: "))
    print("{0} es par --> {1}.".format(n, esPar(n)))

    m = int(input("Introduzca el número de valores: "))
    i = int(input("Introduzca el número inicial: "))
    x = generarPares(m, i)
    y = generarImpares(m, i)
    print("Impares:", y)
    print("Pares:", x)

if __name__ == "__main__":
    main()
