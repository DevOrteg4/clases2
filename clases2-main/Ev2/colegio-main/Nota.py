class Nota():
    def __init__(self,idNota,calificacion,fecha):
        self.idNota=idNota
        self.calificacion=calificacion
        self.fecha=fecha

    def mostrarNota(self):
        return  "\nId Nota        : "+str(self.idNota)+\
                "\nCalificacion   : "+str(self.calificacion)+\
                "\nFecha          : "+self.fecha.mostrarFecha()
                
    def agregarNota(self,idnuevo):
        idnuevo = input()
        calificacion_n = input()
        fecha_n = self.fecha.agregarFecha() #  = fecha
        nota = Nota(idnuevo,calificacion_n,fecha_n)
        return nota

    def modificarNota(self,notaNueva):
        self.calificacion = notaNueva

    def eliminarNota(self):
        self.calificacion = None