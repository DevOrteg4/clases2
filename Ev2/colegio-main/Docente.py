class Docente():
    def __init__(self,idDocente,nombre,asignatura,estudiante):
        self.idDocente=idDocente
        self.nombre=nombre
        self.asignatura=asignatura
        self.estudiante=estudiante

    def mostrarDocente(self):
        return "\nId Docente  : "+str(self.idDocente)+\
               "\nNombre      : "+self.nombre+\
               "\nAsignatura  : "+self.asignatura+\
               "\nEstudiante  : "+self.estudiante.mostrarEstudiante()
