import holidays

# Cargar feriados para México
mx_holidays = holidays.MX()
for date, name in sorted(mx_holidays.items()):
    print(date, name)


# Diccionario de nombres de feriados
rename_holidays = {
    "Año Nuevo": "Año Nuevo",
    "Día de la Constitución": "Día de la Constitución",
    "Natalicio de Benito Juárez": "Día de Benito Juárez",
    "Día del Trabajo": "Día del Trabajo",
    "Día de la Independencia": "Día de la Independencia",
    "Día de la Revolución": "Día de la Revolución",
    "Transmisión del Poder Ejecutivo Federal": "Transmisión del Poder Ejecutivo Federal",
    "Navidad": "Navidad"
}

# Obtener feriados en un rango de fechas
start_date = '2021-01-01'
end_date = '2021-12-31'
holiday_dates = mx_holidays[start_date:end_date]

# Renombrar feriados usando diccionario
renamed_holidays = {rename_holidays[holiday]: date for date, holiday in holiday_dates[0]}


# Imprimir nuevos nombres de feriados
for k, v in renamed_holidays.items():
    print(f"{k}: {v}")
