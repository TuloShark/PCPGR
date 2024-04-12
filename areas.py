from usuario import *
class areas:
    
    areaDesarrollo = []
    areaContabilidad = []
    areaDisenno = []
    areaMarketing = []
    maxDesarrolladores = 0
    maxDiseno = 0
    maxMarketing = 0
    maxContabilidad = 0
    
    def __init__(self, maxAreaDis, maxAreaDevs, maxAreaMarke, maxAreaContabilidad):
       self.maxDesarrolladores = maxAreaDevs
       self.maxDiseno = maxAreaDis
       self.maxMarketing = maxAreaMarke
       self.maxContabilidad = maxAreaContabilidad
    
    def obtenerDatosArea(self, area):
        if(area == 1):
            return self.areaDesarrollo
        elif(area == 2):
            return self.areaDisenno
        elif (area == 3):
            return self.areaMarketing
        elif (area == 4):
            return self.areaContabilidad
    def registrarUsuario(self, usuario, area):
        if (area== 1):
            if(self.maxDesarrolladores == 0):
                return -1
            self.areaDesarrollo.append(usuario)
            self.maxDesarrolladores-= 1
            return 1
        elif(area == 2):
            if(self.maxDiseno == 0):
                return -1
            self.areaDisenno.append(usuario)
            self.maxDiseno-= 1
            return 1
        elif (area == 3):
            if(self.maxMarketing == 0):
                return -1
            self.areaMarketing.append(usuario)
            self.maxMarketing-= 1
            return 1
        elif (area == 4):
            if(self.maxContabilidad == 0):
                return -1
            self.areaContabilidad.append(usuario)
            self.maxContabilidad-= 1
            return 1
    def consultarDisponibles(self,area):
        if(area == 1):
            return self.maxDesarrolladores
        elif(area == 2):
            return self.maxDiseno
        elif (area == 3):
            return self.maxMarketing
        elif (area == 4):
            return self.maxContabilidad
    def eliminarUsuario(self, idUsuario, area):
        idUsuario = int(idUsuario)
        if area == 1:
            for usuario in self.areaDesarrollo:
                if int(usuario.getId()) == idUsuario:
                    self.areaDesarrollo.remove(usuario)
                    self.maxDesarrolladores+= 1
                    return 1
            return -1
        elif area == 2:
            for usuario in self.areaDisenno:
                if int(usuario.getId()) == idUsuario:
                    self.areaDisenno.remove(usuario)
                    self.maxDiseno+= 1
                    return 1
            return -1
        elif area == 3:
            for usuario in self.areaMarketing:
                if int(usuario.getId()) == idUsuario:
                    self.areaMarketing.remove(usuario)
                    self.maxMarketing+= 1
                    return 1
            return -1
        elif area == 4:
            for usuario in self.areaContabilidad:
                if int(usuario.getId()) == idUsuario:
                    self.areaContabilidad.remove(usuario)
                    self.maxContabilidad += 1
                    return 1
            return -1