class Cuadro:
    def __init__(self, autor, cronologia, tecnica, subtecnica, material):
        self.autor = autor
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material

class Replica(Cuadro): 
    def __init__(self, autor, cronologia, tecnica, subtecnica, material):
        super().__init__(autor, cronologia, tecnica, subtecnica, material)
      
class Localizacion_1:
    def __init__(self, museo, ciudad, pais):
        self.museo = museo
        self.ciudad = ciudad
        self.pais = pais

class Localizacion_2(Localizacion_1):
        def __init__(self, museo, ciudad, pais):
            super().__init__(museo, ciudad, pais)

# Crear cuadros
cuadro1 = Cuadro("Leonardo da Vinci", "1503-1506", "Óleo", "Sfumato", "Madera de álamo")
cuadro2 = Replica("Anónimo", "c. 1500", "Óleo", "Pincelada Simple", "Madera de roble")
localizacion1 = Localizacion_1("Museo del Louvre", "París", "Francia")
localizacion2 = Localizacion_2("Museo del Padro", "Madrid", "España")   
   
print(f"Cuadro 1: Autor: {cuadro1.autor}, Cronología: {cuadro1.cronologia}, Técnica: {cuadro1.tecnica}, Subtécnica: {cuadro1.subtecnica}, Material: {cuadro1.material}")
print(f"Cuadro 2 (Réplica): Autor: {cuadro2.autor}, Cronología: {cuadro2.cronologia}, Técnica: {cuadro2.tecnica}, Subtécnica: {cuadro2.subtecnica}, Material: {cuadro2.material}")