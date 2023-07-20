import numpy as np
import pandas as pd
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.flowables import Flowable
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

font_path = 'C:/Users/danie/OneDrive/Escritorio/demopdf/arial/arial.ttf'
pdfmetrics.registerFont(TTFont('Arial', font_path))

# Check the actual font names in the file
for font_name in pdfmetrics.getRegisteredFontNames():
    print(font_name)

class Watermark(Flowable):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        canvas = self.canv
        canvas.saveState()

        canvas.rotate(45)
        canvas.translate(-inch * 4, 0)
        canvas.setFillColorRGB(0.8, 0.8, 0.8, alpha=0.3)

        lines = simpleSplit(self.text, canvas._fontsize, canvas._leading, canvas._pagesize[0])
        text_height = len(lines) * canvas._leading
        text_y = (canvas._pagesize[1] - text_height) / 2

        for line in lines:
            canvas.drawString(100, text_y, line)
            text_y += canvas._leading

        canvas.restoreState()

def crear_pdf_desde_dataframe(dataframe, nombre_archivo):
    # Crear un nuevo documento PDF
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)

    # Convertir el DataFrame a una lista de listas
    data = dataframe.reset_index().values.tolist()  # Agregar el índice como una columna

    # Obtener los nombres de las columnas y el indice del DataFrame
    columnas = dataframe.columns.tolist()
    indice = dataframe.index.name if dataframe.index.name else 'id'




    columnas.insert(0, indice)  # Agregar el nombre d

    data.insert(0, columnas)

    # Crear la tabla y establecer estilos
    tabla = Table(data)
    estilo_cabecera = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ])
    estilo_celda = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 1), (-1, -1), 0.5, colors.black)
    ])
    tabla.setStyle(estilo_cabecera)
    tabla.setStyle(estilo_celda)

    # Agregar encabezado a la tabla
    estilos = getSampleStyleSheet()
    estilo_encabezado = estilos['Heading1']
    estilo_encabezado.alignment = 1  # 0: Izquierda, 1: Centro, 2: Derecha
    encabezado = Paragraph("<b>Tabla de datos</b>", estilo_encabezado)

    # Crear la marca de agua
    marca_agua = Watermark("CONFIDENCIAL")

    # Crear el PageTemplate personalizado
    marco = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 0 * inch, id='normal')
    plantilla = PageTemplate(id='plantilla', frames=[marco], onPage=agregar_pie_pagina, onPageEnd=agregar_marca_agua)

    # Agregar los elementos al documento PDF
    elementos = [encabezado, tabla]
    doc.addPageTemplates([plantilla])
    doc.build(elementos)


def agregar_pie_pagina(canvas, doc):
    numero_pagina = canvas.getPageNumber()
    fecha_actual = date.today().strftime("%d/%m/%Y")

    canvas.saveState()
    estilo_pie_pagina = ParagraphStyle(
        'FooterStyle',
        fontSize=8,
        textColor=colors.black,
        alignment=1
    )
    pie_pagina = Paragraph(f"Página {numero_pagina} - Fecha: {fecha_actual}", estilo_pie_pagina)
    pie_pagina.wrapOn(canvas, doc.width, doc.bottomMargin)
    pie_pagina.drawOn(canvas, doc.leftMargin, doc.bottomMargin - 20)
    canvas.restoreState()

def agregar_marca_agua(canvas, doc):
    # Definir la configuración de la marca de agua
    canvas.saveState()
    canvas.setFont('Arial', 80)
    canvas.setFillGray(0.9, 0.5)
    canvas.rotate(45)
    canvas.drawCentredString(600, 100, 'CONFIDENCIAL')
    canvas.restoreState()



# Ejemplo de uso
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Ana'],
        'Edad': [25, 30, 35, 40, 45],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Zaragoza']}

df = pd.DataFrame(data, columns=['Nombre', 'Edad', 'Ciudad'])
df.index = np.arange(1, len(df) + 1)
print(df)

nombre_archivo = 'ejemplo.pdf'

crear_pdf_desde_dataframe(dataframe=df, nombre_archivo=nombre_archivo)

# Mostrar el PDF
import os
os.system(nombre_archivo)
