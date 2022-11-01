class FechaD():
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def mostrarFecha(self):
        return ("\nDía   : ")+str(self.dia)+\
               ("\nmes   : ")+str(self.mes)+\
               ("\nAño   : ")+str(self.anio)
    
    def agregarFecha(self):
        dia_d = str(input())
        mes_d = str(input())
        anio_d = str(input())
        
        fecha = FechaD(dia_d,mes_d,anio_d)
        return fecha