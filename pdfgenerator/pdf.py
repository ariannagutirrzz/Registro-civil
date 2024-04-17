from fpdf import FPDF

def create_partida_nacimiento(dictValues: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10,'                                      PARTIDA DE NACIMIENTO')
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(20)  # Nueva línea
    text = f"ACTA Nº '{dictValues['id']} ', primera auditoria civil del municipio Maracaibo del estado Zulia, hace constar que se presentó al Despacho la ciudadana de cédula: '{dictValues['padre1_cedula']}' y expuso que el/la niñ@ que presenta de nombre: '{dictValues['nombre']}' de sexo '{dictValues['sexo']}', Nació en la parroquia '{dictValues['parroquia']}' de '{dictValues['lugar_nacimiento']}', el día '{dictValues['fecha_nacimiento']}' a la hora '{dictValues['hora_nacimiento']}'. Siendo su hij@ y del titular de la cédula: '{dictValues['padre2_cedula']}'. Fueron testigos presénciales de éste acto el/la Ciudadano titular de la cédula: '{dictValues['testigo1_cedula']}' y también el/la de la cédula: '{dictValues['testigo2_cedula']}'. Leída la presente acta a exponentes y testigos manifestaron su conformidad y afirman ."
    pdf.multi_cell(0, 7, text)
    pdf.output(name='C:\\Users\\iales\\OneDrive\\Escritorio\\dev\\Registro_civilDB\\pdf\\nacimiento.pdf', dest='F')

def create_acta_matrimonio(dictValues: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10,'                                      ACTA DE MATRIMONIO')
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(20)
    text = f"ACTA Nº '{dictValues['id']}', Este Acta hace constar que los ciudadanos de cédula '{dictValues['contrayente1_cedula']}' y '{dictValues['contrayente2_cedula']}' manifestaron su deseo de contraer matrimonio civil, y acreditaron su capacidad legal para hacerlo. Dicho acto se realiza el día '{dictValues['fecha_ActaMatrimonio']}'. Se citaron para este fin a los padres de ambos contrayentes, los ciudadanos de cédula: '{dictValues['contrayente1_padre1_cedula']}', '{dictValues['contrayente1_padre2_cedula']}', '{dictValues['contrayente2_padre1_cedula']}', '{dictValues['contrayente2_padre2_cedula']}' quienes en presencia del suscrito Notario expresaron su consentimiento al matrimonio."
    pdf.multi_cell(0, 7, text)
    pdf.output(name='C:\\Users\\iales\\OneDrive\\Escritorio\\dev\\Registro_civilDB\\pdf\\matrimonio.pdf', dest='F')

def create_acta_ciudadano(dictValues: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10,'                                      ACTA DE CIUDADANIA')
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(20)
    text = f"Esta acta hace constar que la persona con el Acta de Nacimiento Número '{dictValues['nacimientos_id']}', de nacionalidad '{dictValues['nacionalidad']}', será reconocid@ por parte del Registro Civil ubicado en Maracaibo, Edo. Zulia - Venezuela como ciudadano de dicho país y contará con la Cédula de Identidad número '{dictValues['cedula']}', su estado civil es '{dictValues['estado_civil']}'. Dicho ciudadan@ gozará de todos los derechos, privilegios e inmunidades que en Ley dicha ciudadanía confiere."
    pdf.multi_cell(0, 7, text)
    pdf.output(name='C:\\Users\\iales\\OneDrive\\Escritorio\\dev\\Registro_civilDB\\pdf\\ciudadania.pdf', dest='F')

def create_acta_defuncion(dictValues: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10,'                                      ACTA DE DEFUNCIÓN')
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(20)
    text = f"Esta acta hace constar que el día '{dictValues['fecha_defuncion']}', a las '{dictValues['hora_defuncion']}', falleció en '{dictValues['lugar_defuncion']}', el/la dueñ@ de la cédula de identidad número '{dictValues['cedula']}'. El destino del cadáver fue '{dictValues['destino_cadaver']}'. Se extiende la presente acta a solicitud del interesado para los fines que estime conveniente."
    pdf.multi_cell(0, 7, text)
    pdf.output(name='C:\\Users\\iales\\OneDrive\\Escritorio\\dev\\Registro_civilDB\\pdf\\defuncion.pdf', dest='F')
    
def create_acta_divorcio(dictValues: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(100, 10,'                                      ACTA DE DIVORCIO')
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(20)
    text = f"ACTA Nº '{dictValues['id']}', El señor portador de la cédula de identidad número '{dictValues['divorciado1_cedula']}', y la señora portadora de la cédula de identidad número '{dictValues['divorciado2_cedula']}', contrajeron matrimonio civil declaran bajo juramento el día '{dictValues['fecha_ActaDivorcio']}': Que después de dicho matrimonio, han decidido voluntariamente poner fin a su relación matrimonial. Por lo tanto, solicitan el divorcio por mutuo acuerdo. Se extiende la presente acta de divorcio a solicitud de los interesados para los fines que estimen convenientes."
    pdf.multi_cell(0, 7, text)
    pdf.output(name='C:\\Users\\iales\\OneDrive\\Escritorio\\dev\\Registro_civilDB\\pdf\\divorcio.pdf', dest='F')

def create_stadistics():
    pass