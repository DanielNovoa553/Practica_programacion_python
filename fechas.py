from datetime import datetime, timedelta
import holidays


def es_festivo_mexico_habil_usa_con_ultimo_dia():
    try:
        mexico_holidays = holidays.Mexico()
        usa_holidays = holidays.UnitedStates()

        # Obtener la fecha y hora actual en la zona horaria de México
        # hora_mexico = datetime.now(timezone("America/Mexico_City"))

        # harcodear la fecha para pruebas en local
        hora_mexico = datetime.strptime('2023-11-20 00:00:00', '%Y-%m-%d %H:%M:%S')

        es_festivo_mexico = (
            hora_mexico.strftime("%Y-%m-%d") in mexico_holidays
            or hora_mexico.strftime("%A") in ["Saturday", "Sunday"]
        )
        es_festivo_usa = hora_mexico in usa_holidays

        # Verificar si es festivo en México y hábil en EE. UU.
        if es_festivo_mexico and not es_festivo_usa:
            print(f"{hora_mexico} es festivo en México pero hábil en EE. UU.")
            resultado = True
        elif es_festivo_usa and not es_festivo_mexico:
            print(f"{hora_mexico} es festivo en EE. UU. pero hábil en México.")
            resultado = False
        elif es_festivo_mexico and es_festivo_usa:
            print(f"{hora_mexico} es festivo en México y EE. UU.")
            resultado = False
        else:
            print(f"{hora_mexico} no es festivo en México ni EE. UU.")
            resultado = False

        # Encontrar el último día hábil en México solo si es festivo en México y hábil en EE. UU.
        if es_festivo_mexico and not es_festivo_usa:
            dia_anterior = hora_mexico.date() - timedelta(days=1)

            while dia_anterior.weekday() in [5, 6] or dia_anterior.strftime("%Y-%m-%d") in mexico_holidays:
                dia_anterior -= timedelta(days=1)

            return resultado, dia_anterior
        else:
            return resultado, None

    except Exception as e:
        print(str(e))
        return False, None

# Ejemplo de uso
fecha_feriado, ultimo_dia_habil = es_festivo_mexico_habil_usa_con_ultimo_dia()

print("Es festivo en México y hábil en EE. UU.:", fecha_feriado)
if ultimo_dia_habil:
    print("Último día hábil en México antes de la fecha actual:", ultimo_dia_habil)
else:
    print("No aplica para buscar el último día hábil en México.")


