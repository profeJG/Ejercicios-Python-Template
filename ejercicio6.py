# coding=utf-8
__Author__="José Gaspar Sánchez García"


# Función que determina si un numero es primo.

def esPrimo(numero) :
    contador = 0
    
    if numero==1 :
        contador=contador+1
        return True
    
    def esPrimo(numero):
        if numero == 1:
            return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

            
    if contador == 2 :
        return True
    else :
        return False

# Programa principal
def main():
    print("ES PRIMO")
    n=int(input("Introduzca un numero: "))
    print("{0} es primo --> {1}.".format(n,esPrimo(n)))

if __name__== "__main__" :
   main()
