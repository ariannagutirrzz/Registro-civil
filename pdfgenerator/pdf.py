from fpdf import FPDF

def create_PDF(dictValues):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10,'PARTIDA DE NACIMIENTO')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'Cédula: {dictValues["cedula"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'Nacionalidad: {dictValues["nacionalidad"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'Estado Civil: {dictValues["estado_civil"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'ID de Nacimiento: {dictValues["nacimientos_id"]}')
    pdf.output(name='C:\\Users\\anton\\OneDrive\\Escritorio\\pdf\\ciudadanos.pdf', dest='F')