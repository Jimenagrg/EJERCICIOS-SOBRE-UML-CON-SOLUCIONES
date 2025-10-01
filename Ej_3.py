class Cuadro:
    def __init__(self, titulo, autor, cronologia, tecnica, subtecnica, material, estado):
        self.titulo = titulo
        self.autor = autor
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material
        self.estado = estado
        self.localizacion = None   # relación con Localizacion

    def asignar_localizacion(self, localizacion):
        self.localizacion = localizacion


class Replica(Cuadro): 
    def __init__(self, titulo, autor, cronologia, tecnica, subtecnica, material, estado, original):
        super().__init__(titulo, autor, cronologia, tecnica, subtecnica, material, estado)
        self.original = original   # relación "Es réplica de"


class Localizacion:
    def __init__(self, museo, ciudad, pais):
        self.museo = museo
        self.ciudad = ciudad
        self.pais = pais


# ---------------------------
# Crear objetos según el diagrama
# ---------------------------

# Localizaciones
louvre = Localizacion("Museo del Louvre", "París", "Francia")
prado = Localizacion("Museo del Prado", "Madrid", "España")

# Cuadro original
gioconda = Cuadro(
    "La Gioconda", 
    "Leonardo da Vinci", 
    "1503 - 1516", 
    "Óleo", 
    "Sfumato", 
    "Madera de álamo", 
    "Regular"
)
gioconda.asignar_localizacion(louvre)

# Réplica
replica_gioconda = Replica(
    "Gioconda de El Prado", 
    "Desconocido", 
    "1503 - 1516", 
    "Óleo", 
    "Pincelada simple", 
    "Madera de nogal", 
    "Bueno", 
    original=gioconda
)
replica_gioconda.asignar_localizacion(prado)

# ---------------------------
# Mostrar resultados
# ---------------------------
print(f"{gioconda.titulo} ({gioconda.autor}) se localiza en {gioconda.localizacion.museo}, {gioconda.localizacion.ciudad}, {gioconda.localizacion.pais}")
print(f"{replica_gioconda.titulo} ({replica_gioconda.autor}) es réplica de '{replica_gioconda.original.titulo}' y se localiza en {replica_gioconda.localizacion.museo}, {replica_gioconda.localizacion.ciudad}, {replica_gioconda.localizacion.pais}")
