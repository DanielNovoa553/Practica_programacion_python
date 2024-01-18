from fpdf import FPDF
from api_tabla_hobby.conexion_db import connectdb
# Conexión a la base de datos


con = connectdb()
cursor = con.cursor()

# Ejecutar una consulta SELECT
cursor.execute("SELECT * FROM usuarios")
result = cursor.fetchall()

# Generar el PDF
pdf = FPDF()
pdf.add_page()

# Add the table headers
pdf.set_font("Arial", style="B", size=12)
for i, col in enumerate(cursor.description):
    pdf.cell(40, 10, col[0], 1, align="C")
pdf.cell(0, 10, "", 0, 1,  align="C")

# Add the table data
pdf.set_font("Arial", size=12)
for row in result:
    for item in row:
        pdf.cell(40, 10, str(item), 1, align="C")
    pdf.cell(0, 10, "", 0, 1, align="C")

# Save the PDF
pdf.output("table.pdf", "F")

# Cerrar la conexión a la base de datos
con.close()
cursor.close()
