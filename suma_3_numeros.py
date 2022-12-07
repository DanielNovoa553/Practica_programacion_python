""""
make a class that sum 3 numbers and return the result
"""


class Operaciones:

    def __init__(self):
        pass

    @staticmethod
    def suma(num1, num2, num3):
        result = num1 + num2 + num3
        return result

    @staticmethod
    def resta(num1, num2, num3):
        result = num1 - num2 - num3
        return result

    @staticmethod
    def multiplicacion(num1, num2, num3):
        result = num1 * num2 * num3
        return result

    @staticmethod
    def division(num1, num2, num3):
        result = num1 / num2 / num3
        return result


suma = Operaciones().suma(1, 2, 3)
resta = Operaciones().resta(1, 2, 3)
multiplicacion = Operaciones().multiplicacion(1, 2, 3)
division = round(Operaciones().division(1, 2, 3), 2)

print(f"la suma es: {suma}")
print(f"la resta es: {resta}")
print(f"la multiplicacion es: {multiplicacion}")
print(f"la division es: {division}")
