class Edificio():
    def __init__(self, nombre, culto, lugar, fecha_incio_construccion, fecha_fin_construccion ,primera_consagracion, 
                 fecha_inicio_segunda_etapa, segunda_consagracion, declaracion_BIC, material, estilo):
        self.nombre = nombre
        self.culto = culto
        self.lugar = lugar
        self.fecha_incio_construccion = fecha_incio_construccion
        self.fecha_fin_construccion = fecha_fin_construccion
        self.primera_consagracion = primera_consagracion
        self.fecha_inicio_segunda_etapa = fecha_inicio_segunda_etapa
        self.segunda_consagracion = segunda_consagracion
        self.declaracion_BIC = declaracion_BIC
        self.material = material
        self.estilo = estilo
        self.localizacion = None   # relación con Localizacion

    def asignar_localizacion(self, localizacion):       
        self.localizacion = localizacion    


class Localizacion:
    def __init__(self, ciudad, comunidad, pais):
        self.ciudad = ciudad
        self.comunidad = comunidad
        self.pais = pais
        
# ---------------------------
# Crear objetos según el diagrama

catedral= Edificio(
    "Catedral de Santiago de Compostela", 
    "Católica", 
    "Santiago de Compostela", 
    "1075", 
    "1211", 
    "1211", 
    "1604", 
    "1611", 
    "1931", 
    "Piedra", 
    "Románico, Gótico, Barroco"             
)
catedral.asignar_localizacion(Localizacion("Compostela", "Galicia", "España"))
 
# Localizaciones
localizacion1 = Localizacion("Compostela", "Galicia", "España")



