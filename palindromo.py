from funciones import palindromo


def run():

    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es palindromo')

    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
