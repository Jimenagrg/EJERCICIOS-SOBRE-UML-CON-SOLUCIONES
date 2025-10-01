class Persona: 
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo, id):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.id = id    
    
persona_1 = Persona("Ana", "García", "López", "1990-05-15", "F", "12345678A")


print(f"Nombre: {persona_1.nombre} {persona_1.primer_apellido} {persona_1.segundo_apellido} | Fecha de Nacimiento: {persona_1.fecha_nacimiento}, Sexo: {persona_1.sexo}, ID: {persona_1.id}")


   