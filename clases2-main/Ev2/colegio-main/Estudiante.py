class Estudiante():
    def __init__(self,idEstudiante,nombre,curso,nota):
        self.idEstudiante=idEstudiante
        self.nombre=nombre
        self.curso=curso
        self.nota=nota

    def mostrarEstudiante(self):
        return "\nId Estudiante  : "+str(self.idEstudiante)+\
               "\nNombre         : "+self.nombre+\
               "\nCurso          : "+self.curso+\
               "\nNota           : "+self.nota.mostrarNota()
               
    def agregarEstudiante(self,idnuevo):
        nombre_e = input()
        curso_e = input()
        nota_e = self.nota.agregar_nota()

        persona = Estudiante(idnuevo,nombre_e,curso_e,nota_e)
        return persona

    def mostrarPromedioDelEstudiante(self):
        print(self.nota)