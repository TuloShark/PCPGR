class usuario:
    id = ""
    nombre = ""
    apellido = ""
    cedula = ""
    telefono = ""
    oficina = ""
    sede = ""
    
    def __init__(self, id, nombre, apellido, cedula, telefono, oficina, Sede):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.oficina = oficina
        self.sede = Sede
    def toString(self):
        return (f'Nombre: {self.nombre} Apellido: {self.apellido}, Cedula: {self.cedula}, '
                f'Telefono: {self.telefono}, Oficina: {self.oficina}, Sede: {self.sede}')
    #Seccion GETTER
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getCedula(self):
        return self.cedula
    def getTelefono(self):
        return self.telefono
    def getOficina(self):
        return self.oficina
    def getSede(self):
        return self.sede