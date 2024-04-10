from flask import Flask, render_template, request
import psycopg2

app1 = Flask(__name__)

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="registro_civil_BDD",
    user="postgres",
    password="Blasty1139",
    port= "2345",
    host="localhost"
)

# Función para insertar datos en la base de datos
def insert_into_table(table_name, values):
    try:
        with conn.cursor() as cur:
            columns = ', '.join([f'"{k}"' for k in values.keys()])
            placeholders = ', '.join(['%s'] * len(values))
            query = f"INSERT INTO public.{table_name} ({columns}) VALUES ({placeholders})"
            cur.execute(query, tuple(values.values()))
            conn.commit()
            print("Datos insertados correctamente.")
    except psycopg2.Error as err:
        print(f"Error al insertar datos: {err}")

# Ruta para la página de registro de ciudadanos
@app1.route('/registro_ciudadano', methods=['GET', 'POST'])
def registro_ciudadano():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nacionalidad = request.form['nacionalidad']
        estado_civil = request.form['estado_civil']
        print(cedula)
        # Insertar datos en la base de datos
        insert_into_table('ciudadanos', {'cedula': cedula, 'nacionalidad': nacionalidad, 'estado_civil': estado_civil})
        return 'Datos registrados correctamente.'
    return render_template('registro_ciudadano.html')

if __name__ == 'main':
    app1.run(debug=True)