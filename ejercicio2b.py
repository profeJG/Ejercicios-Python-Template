# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad (edad):
    if(edad>=18):
        return True
    else :
        return False

# Programa principal
def main():
   
    nombre=str(input('Introduzca su nombre : '))
    edad=int(input('Introduza su edad : '))
    if esMayorEdad :
        print('Es mayor de 18,ya puede conducir')
    else : 
        print('Es menor de edad')
        

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()
