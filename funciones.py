import random


def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f"¿Cuantos pesos {tipo_pesos} tienes?: "))
    dolares = round(pesos / valor_dolar, 2)
    print(f"Tienes {dolares} dolares")


def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                  'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'x', 'y', 'z']

    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<',
                '~', '°', '^', '&', '$', '#', '"']

    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def area_triangulo(base, altura):


    return (base * altura) / 2



# Funciones lambda


area_lambda = lambda base, altura: (base * altura) / 2


def max_comi(external_comission, max_commission):
    if external_comission > max_commission:
        raise Exception(
            f"El porcentaje máximo de comisión para este inmueble es de {max_commission}, por favor verifica la información")

    else:
        print(f"todo bien")

