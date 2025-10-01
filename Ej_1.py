class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro

    def __str__(self):
        return f"Círculo -> Color: {self.color}, Diámetro: {self.diametro}"


class Elipse:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def __str__(self):
        return f"Elipse -> Color: {self.color}, Eje Mayor: {self.eje_mayor}, Eje Menor: {self.eje_menor}"


class Rectangulo:
    def __init__(self, color, longitud, anchura):
        self.color = color
        self.longitud = longitud
        self.anchura = anchura

    def __str__(self):
        return f"Rectángulo -> Color: {self.color}, Longitud: {self.longitud}, Anchura: {self.anchura}"


class Cuadrado:
    def __init__(self, color, longitud):
        self.color = color
        self.longitud = longitud   # solo tiene color y longitud

    def __str__(self):
        return f"Cuadrado -> Color: {self.color}, Longitud: {self.longitud}"

c1 = Circulo("Negro", 1)
e1 = Elipse("Amarillo", 3, 1)
r1 = Rectangulo("Naranja", 3, 1)
c2 = Cuadrado("Azul", 2)

print(c1)
print(e1)
print(r1)
print(c2)