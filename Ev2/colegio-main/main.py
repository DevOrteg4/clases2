from Fecha import Fecha
from Nota import Nota
from Estudiante import Estudiante
from Docente import Docente

lista = []
while True:
    print("\n1.Agregar Docente")
    print("\n2.Agregar Estudiante")
    print("\n3.Modificar Nota")
    print("\n4.Eliminar Nota")
    print("\n5.Mostrar Promedio de un Estudiante")
    print("\n6.Finalizar")
    opcion=int(input("Ingrese su opcion (1-6)"))
    if opcion ==1:
        idDocente = int(input("Ingrese Id: "))
        nombre = input("Nombre: ")
        asignatura = input("Asignatura: ")
        estudiante = input("Estudiante: ")
        p=Docente(idDocente,nombre,asignatura,estudiante)
        lista.append(p)
        print("\nDocente agregado correctamente...")