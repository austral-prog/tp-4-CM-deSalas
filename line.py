import math
def line():
    A = float(input("Ingrese el coeficiente A:"))
    B = float(input("Ingrese el coeficiente B:"))
    X1 = float(input("Ingrese el coeficiente X1:"))
    X2 = float(input("Ingrese el coeficiente X2:"))
    Y1 = (A * X1 + B)
    Y2 = (A * X2 + B)
    distancia = math.sqrt((Y2-Y1)**2+(X2-X1)**2)
    print(f"Para la siguiente ecuación:\n\t y = {A}x + {B}")
    print(f"Dados los siguientes puntos:\n\t P1 = ({X1}, {Y1}) \n\t P2 = ({X2}, {Y2})")
    print(f"La distancia entre ellos: {distancia}")
