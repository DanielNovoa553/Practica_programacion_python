"""
Funcion que calcula la distancia entre dos puntos
"""
class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    cordenada_1 = Coordenada(3,30)
    cordenada_2 = Coordenada(4,8)

    print(cordenada_1.distancia(cordenada_2))
    print(isinstance(cordenada_2, Coordenada))


