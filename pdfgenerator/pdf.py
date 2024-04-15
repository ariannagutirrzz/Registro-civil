from fpdf import FPDF

def create_partida_nacimiento(dictValues):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10,'PARTIDA DE NACIMIENTO')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'ID: {dictValues["id"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'NOMBRE: {dictValues["nombre"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'SEXO: {dictValues["sexo"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'FECHA DE NACIMIENTO: {dictValues["fecha_nacimiento"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'HORA DE NACIMIENTO: {dictValues["hora_nacimiento"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'LUGAR DE NACIMIENTO: {dictValues["lugar_nacimiento"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'CEDULA PADRE 1: {dictValues["padre1_cedula"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'CEDULA PADRE 2: {dictValues["padre2_cedula"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'TESTIGO 1 CEDULA: {dictValues["testigo1_cedula"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'TESTIGO 2 CEDULA: {dictValues["testigo2_cedula"]}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'PARROQUIA: {dictValues["parroquia"]}')
    pdf.output(name='C:\\Users\\anton\\OneDrive\\Escritorio\\pdf\\ciudadanos.pdf', dest='F')

def create_stadistics():
    pass