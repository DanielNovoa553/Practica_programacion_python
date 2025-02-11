import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date, timedelta
import time
import threading

# Fecha de inicio
fecha_inicio = date(2025, 2, 2)


def calcular_dias_sobrio():
    """Calcula cuántos días han pasado desde la fecha de inicio."""
    hoy = date.today()
    dias_sobrio = (hoy - fecha_inicio).days
    return dias_sobrio


def mostrar_mensaje():
    """Muestra la notificación con los días sobrios."""
    dias = calcular_dias_sobrio()
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Progreso", f"Llevas {dias} días sobrio. ¡Sigue así!")
    root.destroy()


def esperar_hora_fija():
    """Espera hasta la 1:00 PM y luego ejecuta la notificación diariamente."""
    while True:
        ahora = datetime.now()
        proxima_ejecucion = datetime.combine(ahora.date(), datetime.min.time()) + timedelta(hours=13)  # 1:00 PM

        if ahora > proxima_ejecucion:
            proxima_ejecucion += timedelta(days=1)  # Mueve la ejecución al día siguiente

        segundos_espera = (proxima_ejecucion - ahora).total_seconds()
        time.sleep(segundos_espera)  # Espera hasta la 1:00 PM
        mostrar_mensaje()


# Ejecutar la programación en un hilo para que no bloquee el programa
hilo = threading.Thread(target=esperar_hora_fija, daemon=True)
hilo.start()

# Muestra el mensaje inmediatamente al iniciar el script (opcional)
mostrar_mensaje()
