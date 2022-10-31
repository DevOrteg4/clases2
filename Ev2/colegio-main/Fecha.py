class Fecha():
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def mostrarFecha(self):
        return ("\nDía   : ")+str(self.dia)+\
               ("\nmes   : ")+str(self.mes)+\
               ("\nAño   : ")+str(self.anio)
               