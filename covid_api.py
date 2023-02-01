import os
import tkinter as tk
import requests
import json
from datetime import datetime
import pandas as pd

def get_covid_data():
    # Hacer la solicitud HTTP GET a la API
    response = requests.get("https://disease.sh/v3/covid-19/all")
    # Verificar que la respuesta sea exitosa
    if response.status_code == 200:
        # Analizar el contenido JSON de la respuesta
        data = json.loads(response.content)
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Extraer la información que necesitas
        total_cases = data["cases"]
        total_deaths = data["deaths"]
        today_cases = data["todayCases"]
        today_deaths = data["todayDeaths"]
        recovered = data["recovered"]
        today_recovered = data["todayRecovered"]
        active = data["active"]
        critical = data["critical"]
        population = data["population"]
        affected_countries = data["affectedCountries"]
        root = tk.Tk()
        root.title("Covid-19 Report")
        root.geometry("600x450")
        f = ("poppins", 14, "bold")
        f2 = ("poppins", 18, "bold", "italic")
        f3 = ("poppins", 10, "bold")
        label2 = tk.Label(root, font=f2, text="Reporte Covid 19" ,fg="red")
        label2.pack(side="top", pady=10)
        label = tk.Label(root, font=f, text="Casos Totales: " +  str(total_cases)+"\n" + "Muertes Totales: " +
                                            str(total_deaths)+"\n" + "Casos Hoy: " + str(today_cases)+"\n" +
                                            "Muertes Hoy: " + str(today_deaths)+"\n" + "Recuperados: " +
                                            str(recovered)+"\n" + "Recuperados Hoy: " + str(today_recovered)+
                                            "\n" + "Activos: " + str(active)+"\n" + "Críticos: " + str(critical)+
                                            "\n" + "Población: " + str(population)+"\n" + "Países Afectados: " +
                                            str(affected_countries))
        label.pack()
        label3 = tk.Label(root, font=f3, text="Reporte Covid 19", fg="grey")
        label3.config(text="Fecha: " + str(date))
        label3.pack(side="bottom", pady=15)

        root.mainloop()

        print("Información COVID-19")
        print(f"Casos Totales: {total_cases}")
        print(f"Muertes Totales: {total_deaths}")
        print(f"Casos de Hoy: {today_cases}")
        print(f"Muertes de Hoy: {today_deaths}")
        print(f"Recuperados: {recovered}")
        print(f"Recuperados de Hoy: {today_recovered}")
        print(f"Activos: {active}")
        print(f"Críticos: {critical}")
        print(f"Población: {population}")
        print(f"Países Afectados: {affected_countries}")

        # df = pd.DataFrame(data, index=[0])
        # df.drop(["updated", "tests", "testsPerOneMillion", "oneCasePerPeople", "oneDeathPerPeople", "oneTestPerPeople",
        #          "activePerOneMillion", "recoveredPerOneMillion", "criticalPerOneMillion", "casesPerOneMillion",
        #          "deathsPerOneMillion" ], axis=1, inplace=True)
        # print(df)
        # writer = pd.ExcelWriter("covid19.xlsx")
        # df.to_excel( "covid19.xlsx", index=False, header=True, freeze_panes=(1, 0), engine='xlsxwriter', sheet_name="covid19")
        # print("Datos exportados exitosamente a --> covid19.xlsx")
        # filename = os.path.abspath("covid19.xlsx")
        # os.startfile(filename)

    else:
        # Manejar el error
        print("Error al obtener la información:", response.status_code)


if __name__ == '__main__':
    get_covid_data()
