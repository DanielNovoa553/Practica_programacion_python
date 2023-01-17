# hacer un programa que lea un archivo json y lo imprima en pantalla


import json

with open('datos.json') as file:
    data = json.load(file)

print(data)

lista = []
lista.append(data)  # Agrega el diccionario data al final de la lista
print(lista)

#ordenar un diccionario por clave para generar datos en formato json con dumps

import json

diccionario = {'7': '5', '1': 2, '3': 4, '2': 3, '6': 1, '4': 6, '5': 7}

print(json.dumps("diccionario ordenado por clave: "))
print(json.dumps(diccionario, sort_keys=True, indent=4))    # Imprime el diccionario ordenado por clave


# hacer un programa que sume 3 numeros y haga pruebas unitarias

import unittest # Importa la librería unittest


def suma(x, y, z):  # Función suma
    return x + y + z    # Retorna la suma de los 3 números


class TestSuma(unittest.TestCase):  # Crea la clase TestSuma que hereda de unittest.TestCase
    def test_suma(self):    # Crea el método test_suma
        self.assertEqual(suma(3, 3, 3), 9, "Deberia ser 9")     # Prueba que la suma de 3 + 3 + 3 sea 9


if __name__ == '__main__':  # Si el archivo es ejecutado directamente
    unittest.main()    # Ejecuta el método main de unittest



# hacer un programa que lea un array de numpy y lo imprima en pantalla

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 =np.arange(1, 11)

print(array)

