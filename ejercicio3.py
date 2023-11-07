# coding=utf-8
__Author__="José Gaspar Sánchez García"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# Implemente función obtenerCalificacion
def obtenerCalificaion(nota) :
    calificacion="Incorrecta"
   # Implemente aquí ... Si (condición) entonces ... sino ... si (condición) entonces ... sino ...
   
    if(nota>=0 and nota<3):
        return "Muy deficiente"
    elif(nota>=3 and nota<5):
        return"Insuficiente"
    elif(nota>=5 and nota<6):
        return"Suficiente"
    elif(nota>=6 and nota<7):
        return"Bien"
    elif(nota>=7 and nota<9):
        return"Notable"
    elif(nota>=9 and nota<=10):
        return"Sobresaliente"
        
    return calificacion

# Programa principal
def main():
    n=int(input("Introduzca la nota: "));
    print('Calificación: '+obtenerCalificaion(n));
if __name__== "__main__" :
   main()
