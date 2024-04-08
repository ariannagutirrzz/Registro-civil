import psycopg2

#Clase para la conexion de la base de datos
class UserConnection():
    conn = None
    #Abre la conexiona a la BDD
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="carnalito_db", #Nombre de la BDD en tu pc
                user="antonio", #Nombre del user que tengas en tu pc
                password="123456" #Contrasena que tengas en tu pc
            )
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.close()

    def dictfetchall(self, cur):
    #Devuelve todas las filas de un cursor como un diccionario
        desc = cur.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cur.fetchall()
        ]
    
    #Query para insertar datos
    def insert_into_table(self, table_name: str, values: dict):
        try:
            with self.conn.cursor() as cur:
                columns = ', '.join(values.keys())
                placeholders = ', '.join(['%s'] * len(values))
                query = f"INSERT INTO public.{table_name} ({columns}) VALUES ({placeholders})"
                cur.execute(query, tuple(values.values()))
                self.conn.commit()
                print("Datos insertados correctamente.")
        except psycopg2.Error as err:
            print(f"Error al insertar datos: {err}")

    def read(self, table_name: str):
        try:
            with self.conn.cursor() as cur:
                query = f"SELECT * FROM public.{table_name}"
                cur.execute(query)
                data = self.dictfetchall(cur)
                if data is not None:
                    return data
                else:
                    print("Data is None")
        except psycopg2.Error as err:
            print("Error al leer datos: ", err)

    #Cierra la conexion a la BDD al finalizar la ejecucion
    def __del__(self):
        self.conn.close()    