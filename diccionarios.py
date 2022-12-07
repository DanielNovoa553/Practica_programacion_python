def run():

    poblacion_paises = {

        'Argentina': 44567913,
        'Brasil': 210863834,
        'Colombia': 34556778,
        'venezuela': 32456789

    }

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes")


if __name__ == '__main__':
    run()
