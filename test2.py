# hacer una funcion con kwargs que sume n numeros y retorne la suma y haga pruebas unitarias con unittest
import unittest

numeros = {

    "numero1": 1,
    "numero2": 2,
    "numero3": 3,
    "numero4": 4,
    "numero5": 5,
    "numero6": 6,
}


def sumar_numeros(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma += value
    return suma


adiccion = sumar_numeros(**numeros)
print(adiccion)


class TestSumarNumeros(unittest.TestCase):
    def test_sumar_numeros(self):
        """
        Test sumar_numeros function
        Returns:
            None
        """
        self.assertEqual(sumar_numeros(**numeros),adiccion)


if __name__ == '__main__':
    print(f"La suma de los numeros es: {sumar_numeros(**numeros)}")
    unittest.main()

