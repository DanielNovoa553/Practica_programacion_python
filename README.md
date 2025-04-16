# 🧪 DanielNovoa553 - Proyectos en Python

Este repositorio es una recopilación de proyectos, pruebas de concepto, scripts personales y ejemplos desarrollados principalmente con **Python**. Incluye desde pequeños juegos y utilidades de consola, hasta APIs REST con **Flask** y **FastAPI**, análisis de datos, generación de PDFs, exportación de archivos y más.

---

## 📁 Estructura del repositorio

A continuación, un resumen de los directorios y archivos más relevantes:

| Carpeta / Archivo        | Descripción |
|--------------------------|-------------|
| `apiCovid19All/`         | API para consultar datos del COVID-19. |
| `api_dias_habiles/`      | API para cálculo de días hábiles. |
| `api_login/`             | API de autenticación simple con JWT. |
| `api_tabla_hobby/`       | Exportación de hobbies con formato Excel. |
| `cuenta_dias/`           | Proyecto para calcular fechas y días entre eventos. |
| `fastapidemo/`           | Pruebas con FastAPI. |
| `gato_game/`             | Juego "Atrapa el gato" en consola. |
| `login_modal/`           | Demo de login con modales y validaciones. |
| `tic_tac_toe/`           | Juego clásico del tres en raya (gato). |
| `SecurityVideo/`         | Código de prueba para video con seguridad. |
| `pdf_df/`                | Generación de PDFs desde DataFrames. |
| `.github/workflows/`     | Flujo de trabajo de GitHub Actions para publicación. |
| `.env`                   | Variables de entorno (no incluidas por seguridad). |
| `Pipfile / Pipfile.lock` | Dependencias del entorno para proyectos FastAPI. |

También hay scripts sueltos como:

- `exportpdf.py`, `exportxls.py`, `export_pd_excel.py`: exportación de datos en diferentes formatos.
- `get_holidays.py`, `catalogo_holidays.py`: manejo de fechas y días festivos.
- `generador_contrasenas.py`, `palindromo.py`, `adivina_el_numero.py`: scripts de consola.
- `relacion_tabla*.py`: ejemplos de relaciones de tablas con pandas o estructuras personalizadas.
- `dynamo.py`, `datos.json`, `data.json`: ejemplos con datos anidados o DynamoDB.

---

## 🛠 Tecnologías usadas

- Python 3.x
- Flask
- FastAPI
- Pandas
- Tkinter
- PyPDF2 / FPDF
- OpenPyXL
- Unittest / Pytest
- Docker (en algunos proyectos)

---

## 🚀 Cómo usar

Cada proyecto tiene su propia lógica de ejecución. Recomendaciones generales:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/DanielNovoa553/DanielNovoa553.git
   cd DanielNovoa553

2. Crea un entorno virtual y activa:
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala dependencias:
pip install -r requirements.txt

4. Corre los scripts según sea necesario:
python api_dias_habiles/app.py
python gato_game/main.py

👨‍💻 Autor
Daniel Armando Novoa Zambrano
Ingeniero en informática | Backend Developer
📍 Ciudad de México | 
🛠 Experto en desarrollo backend, APIs, análisis de datos y automatización.

📝 Licencia
MIT
Este repositorio es una mezcla entre laboratorio de pruebas, utilidades personales y proyectos compartibles para demostrar conocimiento técnico en diferentes áreas de Python. ¡Explora libremente!
