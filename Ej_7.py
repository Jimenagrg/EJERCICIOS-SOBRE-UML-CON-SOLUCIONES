class Persona: 
    def __init__(self, nombre_dado, nombre_familia, sexo, fecha_nacimiento, lugar_nacimiento,fecha_defuncion, lugar_defuncion):
        self.nombre_dado = nombre_dado
        self.nombre_familia = nombre_familia
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.lugar_defuncion = lugar_defuncion
    
class Ocupacion:
    def __init__(self, nombre_ocupacion, desde, hasta):
        self.nombre_ocupacion = nombre_ocupacion
        self.desde = desde
        self.hasta = hasta
        self.persona = None   # relación con Persona
    def asignar_persona(self, persona):
        self.persona = persona
persona_1 = Persona("Ana", "García", "López", "1990-05-15", "F", "12345678A")
ocupacion_1 = Ocupacion("Ingeniera", "2013", "2023)
                        
class Documento:
    def __init__(self, titulo, tipo, fecha):
        self.titulo = titulo
        self.tipo = tipo
        self.fecha = fecha
        self.autor = None   # relación con Persona
    def asignar_autor(self, persona):
        self.autor = persona
documento_1 = Documento("Proyecto X", "Informe", "2020-06-30")
ocupacion_1.asignar_persona(persona_1)
documento_1.asignar_autor(persona_1)
print(f"Nombre: {persona_1.nombre_dado} {persona_1.nombre_familia} | Fecha de Nacimiento: {persona_1.fecha_nacimiento}, Sexo: {


class Evento: 
    def __init__(self, nombre_evento, momento, descripcion):
        self.nombre_evento = nombre_evento
        self.momento = momento
        self.descripcion = descripcion
        self.persona = None   # relación con Persona
    def asignar_persona(self, persona):
        self.persona = persona
evento_1 = Evento("Graduación", "2013-05-15", "Graduación universitaria")
evento_1.asignar_persona(persona_1)
print(f"Evento: {evento_1.nombre_evento} | Momento: {evento_1.momento}, Descripción: {evento_1.descripcion}, Persona: {evento_1.persona.nombre_dado} {evento_1.persona.nombre_familia}")

class Lugar:
    def __init__(self, nombre, direccion, pais):
        self.nombre = nombre
        self.direccion = direccion
        self.pais = pais
lugar_1 = Lugar("Universidad X", "Calle Falsa 123", "España")
print(f"Lugar: {lugar_1.nombre} | Dirección: {lugar_1.direccion}, País: {lugar_1.pais}")persona_1.sexo}")





class Persona:
    def __init__(self, nombre_dado, nombre_familia, sexo, fecha_nacimiento, lugar_nacimiento,
                 fecha_defuncion=None, lugar_defuncion=None):
        self.nombre_dado = nombre_dado
        self.nombre_familia = nombre_familia
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.lugar_defuncion = lugar_defuncion

        # Relaciones
        self.ocupaciones = []
        self.documentos = []
        self.eventos = []
        self.lugares_visitados = []

    def asignar_ocupacion(self, ocupacion):
        self.ocupaciones.append(ocupacion)
        ocupacion.persona = self

    def asignar_documento(self, documento):
        self.documentos.append(documento)
        documento.autor = self

    def asignar_evento(self, evento):
        self.eventos.append(evento)
        evento.participantes.append(self)

    def visitar_lugar(self, lugar):
        self.lugares_visitados.append(lugar)

    def __str__(self):
        return f"{self.nombre_dado} {self.nombre_familia} ({self.sexo})"


class Ocupacion:
    def __init__(self, nombre, desde, hasta=None):
        self.nombre = nombre
        self.desde = desde
        self.hasta = hasta
        self.persona = None

    def __str__(self):
        return f"{self.nombre} desde {self.desde} hasta {self.hasta if self.hasta else 'actualidad'}"


class Documento:
    def __init__(self, titulo, tipo, fecha_publicacion=None):
        self.titulo = titulo
        self.tipo = tipo
        self.fecha_publicacion = fecha_publicacion
        self.autor = None

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"


class Evento:
    def __init__(self, nombre, momento, descripcion=None):
        self.nombre = nombre
        self.momento = momento
        self.descripcion = descripcion
        self.participantes = []  # Lista de personas

    def __str__(self):
        return f"{self.nombre} en {self.momento}"


class Lugar:
    def __init__(self, nombre, direccion=None, pais=None):
        self.nombre = nombre
        self.direccion = direccion
        self.pais = pais

    def __str__(self):
        return f"{self.nombre}, {self.pais}"


# ------------------ Ejemplo de uso ------------------

# Persona
persona_1 = Persona("Ana", "García", "F", "1990-05-15", "Madrid")

# Ocupación
ocupacion_1 = Ocupacion("Ingeniera", "2013", "2023")
persona_1.asignar_ocupacion(ocupacion_1)

# Documento
documento_1 = Documento("Proyecto X", "Informe", "2020-06-30")
persona_1.asignar_documento(documento_1)

# Evento
evento_1 = Evento("Graduación", "2013-05-15", "Graduación universitaria")
persona_1.asignar_evento(evento_1)

# Lugar
lugar_1 = Lugar("Universidad X", "Calle Falsa 123", "España")
persona_1.visitar_lugar(lugar_1)

# ------------------ Imprimir resultados ------------------
print(f"Persona: {persona_1}")
print(f"  Ocupación: {ocupacion_1}")
print(f"  Documento: {documento_1}")
print(f"  Evento: {evento_1}")
print(f"  Visitó: {lugar_1}")




        
