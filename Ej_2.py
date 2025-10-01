
class Persona:
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo

class Matrimonio:
    def __init__(self, conyuge1, conyuge2):
        self.conyuge1 = conyuge1
        self.conyuge2 = conyuge2


class Hijo(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo, padre, madre):
        super().__init__(nombre, apellido, apellido_nacimiento, sexo)
        self.padre = padre
        self.madre = madre

# Crear personas
kate = Persona("Kate", "Windsor", "Middleton", "F")
guillermo = Persona("Guillermo", "Windsor", "Windsor", "M")
carlos = Persona("Carlos", "Windsor", "Windsor", "M")
diana = Persona("Diana", "de Gales", "Spencer", "F")

# Matrimonio entre Kate y Guillermo
matrimonio_kate_guillermo = Matrimonio(kate, guillermo)

# Matrimonio entre Carlos y Diana
matrimonio_carlos_diana = Matrimonio(carlos, diana)

# Guillermo es hijo de Carlos y Diana
guillermo = Hijo("Guillermo", "Windsor", "Windsor", "M", carlos, diana)