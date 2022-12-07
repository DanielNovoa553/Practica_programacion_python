
class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return (x_diff + y_diff)**0.5


class Lavadora:

    def __init__(self): 
        pass

    def lavar(self, temperatura='Super caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        self._secar_ropa()
        self._ciclo_terminado()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f"Llenado el tanque con agua {temperatura}!!!")

    def _anadir_jabon(self):
        print("Añadiendo Jabon!!!")

    def _lavar(self):
        print('Lavando la Ropa!!')

    def _centrifugar(self):
        print('Centrifugando la ropa!!!')

    def _secar_ropa(self):
        print ("Secando la Ropa!!!")

    def _ciclo_terminado(self):
        print("Ciclo de lavado terminado!!!")

