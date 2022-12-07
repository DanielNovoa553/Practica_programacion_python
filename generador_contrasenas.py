from funciones import generar_contrasena


def run():

    contrasena = generar_contrasena()
    print(f"tu nueva contraseña es: {contrasena}")


if __name__ == '__main__':
    run()
