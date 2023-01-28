from test2 import *


class TestSumarNumeros(unittest.TestCase):
    def test_sumar_numeros(self):
        """
        Test sumar_numeros function
        Returns:
            None
        """
        self.assertEqual(sumar_numeros(**numeros), adiccion)


if __name__ == '__main__':
    unittest.main()