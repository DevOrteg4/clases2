from Estudiante import Estudiante


class Docente():
    def __init__(self,idDocente,nombre,asignatura,estudiante):
        self.idDocente=idDocente
        self.nombre=nombre
        self.asignatura=asignatura
        self.estudiante=estudiante
        

    def mostrar_docente(self):
        return "\nId Docente  : "+str(self.idDocente)+\
               "\nNombre      : "+self.nombre+\
               "\nAsignatura  : "+self.asignatura+\
               "\nEstudiante  : "+self.estudiante.mostrarEstudiante()

    def agregar_docente(self,lista,id_nuevo):
        nombre_d = input()
        asignatura_d = input()
        estudiante_d = self.estudiante.agregar_estudiante(id_nuevo)

        persona = Docente(id_nuevo,nombre_d,asignatura_d,estudiante_d)
        lista.append(persona)
        return lista
