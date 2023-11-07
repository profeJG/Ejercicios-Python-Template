# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    return x+y

def resta(x,y) :
    return x-y

def multiplica(x,y) :
    return x*y

def divide(x,y) :
    return x/y

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))

        if opcion == 1 :
            s1=int(input("Introduzca el primer sumando: "))
            s2=int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1,s2,suma(s1,s2)))
        elif opcion == 2 :
            minuendo=int(input("Introduzca el minuendo: "))
            sustraendo=int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo,sustraendo,resta(minuendo,sustraendo)))
        elif opcion ==3 : 
            numero=int(input("Introduza un numero:  "))
            multiplo=int(input("Introduza el multiplo:  "))
            print("La multp. de {0} * {1}= {2}.".format(numero,multiplo,multiplica(numero,multiplo)))
        elif opcion ==4 : 
            dividendo=int(input("Introduza  el dividendo:  "))
            divisor=int(input("Introduza el divisor:  "))
            print("La division  de {0}/{1} ={2}.".format(dividendo,divisor,divide(dividendo,divisor)))
        elif opcion !=0 :
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()
