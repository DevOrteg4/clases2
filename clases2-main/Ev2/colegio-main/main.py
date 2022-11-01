from Fecha import Fecha
from Nota import Nota
from Estudiante import Estudiante
from Docente import Docente

lista = []

fecha = Fecha(20,10,2018)
nota = Nota(1,6.0,fecha)
estudiante = Estudiante(1,"felipe","1A",nota)
docente = Docente(1,"gonzalo","quimica",estudiante)
lista.append(docente)

while True:
    print("\n1.Agregar Docente")
    print("\n2.Agregar Estudiante")
    print("\n3.Modificar Nota")
    print("\n4.Eliminar Nota")
    print("\n5.Mostrar Promedio de un Estudiante")
    print("\n6.Finalizar")
        
    try:
        opcion=int(input("Ingrese su opcion (1-6)"))
        
        if opcion ==1:
            pass
        
        
    except:
        print("pone un numero del 1 al 6 aweonao")
    
    
    