import psycopg2
from datetime import date

#Clase para la conexion de la base de datos
class UserConnection():
    conn = None
    #Abre la conexiona a la BDD
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="RegistroBD", #Nombre de la BDD en tu pc
                user="postgres", #Nombre del user que tengas en tu pc
                password="12345", #Contrasena que tengas en tu pc
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
                columns = ', '.join([f'"{k}"' for k in values.keys()]) #Le agrega comillas dobles a cada columna de la BDD, ya que pgadmine es case sesitive
                placeholders = ', '.join(['%s'] * len(values))
                query = f"INSERT INTO public.{table_name} ({columns}) VALUES ({placeholders})"
                cur.execute(query, tuple(values.values()))
                self.conn.commit()
                print("Datos insertados correctamente.")
        except psycopg2.Error as err:
            print(f"Error al insertar datos: {err}")
            self.conn.rollback()

    #Query para leer los datos
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
            self.conn.rollback()

    def read_ciudadano(self, table_name: str, table_name2: str):
        try:
            with self.conn.cursor() as cur:
                query = f"SELECT cedula, nacionalidad, estado_civil, nacimientos_id, nombre FROM public.{table_name} INNER JOIN public.{table_name2} ON public.{table_name}.nacimientos_id = public.{table_name2}.id;"
                cur.execute(query)
                data = self.dictfetchall(cur)
                if data is not None:
                    return data
                else:
                    print("Data is None")
        except psycopg2.Error as err:
            print("Error al leer datos: ", err)
            self.conn.rollback()
    
    def read_by_cedula(self, table_name: str, cedula: int):
        try:
            with self.conn.cursor() as cur:
                query = f"SELECT * FROM public.{table_name} WHERE cedula = {cedula}"
                cur.execute(query)
                data = self.dictfetchall(cur)
                if data is not None:
                    return data
                else:
                    print("Data is None")
        except psycopg2.Error as err:
            print("Error al leer datos: ", err)
            self.conn.rollback()

    def read_by_id(self, table_name: str,  table_id: int):
        try:
            with self.conn.cursor() as cur:
                query = f"SELECT * FROM public.{table_name} WHERE id = {table_id}"
                cur.execute(query)
                data = self.dictfetchall(cur)
                if data is not None:
                    return data
                else:
                    print("Data is None")
        except psycopg2.Error as err:
            print("Error al leer datos: ", err)
            self.conn.rollback()

    #Query para eliminar datos por id
    def delete_id(self, table_name: str, table_id: int):
        try:
            with self.conn.cursor() as cur:
                query = f"DELETE FROM public.{table_name} WHERE id = {table_id}"
                cur.execute(query)
                self.conn.commit()
                print(f"Registro con id {table_id} eliminado correctamente de la tabla {table_name}.")
        except psycopg2.Error as err:
            print("Error al eliminar datos: ", err)
            self.conn.rollback()

    #Query para eliminar datos por cedula
    def delete_cedula(self, table_name: str, table_cedula: int):
        try:
            with self.conn.cursor() as cur:
                query = f"DELETE FROM public.{table_name} WHERE cedula = {table_cedula}"
                cur.execute(query)
                self.conn.commit()
                print(f"Registro con cedula {table_cedula} eliminado correctamente de la tabla {table_name}.")
        except psycopg2.Error as err:
            print("Error al eliminar datos: ", err)
            self.conn.rollback()

    #Query para actualizar datos por id
    def update_field_id(self, table_name: str, table_id: int, new_values: dict):
        try:
            with self.conn.cursor() as cur:
                set_clause = ', '.join([f'"{column}" = %s' for column in new_values.keys()])
                values = list(new_values.values())
                query = f"UPDATE public.{table_name} SET {set_clause} WHERE id = {table_id}"
                cur.execute(query, tuple(values))
                self.conn.commit()
                print(f"Registro con cedula {table_id} actualizado correctamente de la tabla {table_name}.")
        except psycopg2.Error as err:
            print("Error al actualizar datos: ", err)
            self.conn.rollback()

    #Query para actualizar datos por id
    def update_field_cedula(self, table_name: str, table_cedula: int, new_values: dict):
        try:
            with self.conn.cursor() as cur:
                set_clause = ', '.join([f'"{column}" = %s' for column in new_values.keys()])
                values = list(new_values.values())
                query = f"UPDATE public.{table_name} SET {set_clause} WHERE cedula = {table_cedula}"
                cur.execute(query, tuple(values))
                self.conn.commit()
                print(f"Registro con cedula {table_cedula} actualizado correctamente de la tabla {table_name}.")
        except psycopg2.Error as err:
            print("Error al actualizar datos: ", err)
            self.conn.rollback()

    #Query para estadistica del total en una tabla
    def stadistics(self, date_start: date, date_end: date, lugar_nacimiento: str, parroquia: str):
        try:
            with self.conn.cursor() as cur:
                queries = [
                            "SELECT COUNT(*) AS total_nacimientos FROM public.\"Nacimientos\";",
                            "SELECT COUNT(*) AS total_hombres FROM public.\"Nacimientos\" WHERE sexo = 'Masculino';",
                            "SELECT COUNT(*) AS total_mujeres FROM public.\"Nacimientos\" WHERE sexo = 'Femenino';",
                            "SELECT COUNT(*) AS total_otros FROM public.\"Nacimientos\" WHERE sexo = 'Otro';",
                            f"SELECT COUNT(fecha_nacimiento) AS nacidos_mes FROM public.\"Nacimientos\" WHERE fecha_nacimiento >= TO_DATE('{date_start.strftime('%Y-%m-%d')}', 'YYYY-MM-DD') AND fecha_nacimiento <= TO_DATE('{date_end.strftime('%Y-%m-%d')}', 'YYYY-MM-DD');",
                            f"SELECT COUNT(lugar_nacimiento) AS nacidos_{lugar_nacimiento} FROM public.\"Nacimientos\" WHERE lugar_nacimiento = '{lugar_nacimiento}';",
                            f"SELECT COUNT(parroquia) AS nacidos_{parroquia} FROM public.\"Nacimientos\" WHERE parroquia = '{parroquia}';",
                            "SELECT COUNT(*) AS total_ciudadanos FROM public.\"Ciudadanos\";",
                            "SELECT COUNT(nacionalidad) AS total_venezolanos FROM public.\"Ciudadanos\" WHERE nacionalidad = 'Venezolana';",
                            "SELECT COUNT(estado_civil) AS total_solteros FROM public.\"Ciudadanos\" WHERE estado_civil = 'Soltero';",
                            "SELECT COUNT(estado_civil) AS total_solteros FROM public.\"Ciudadanos\" WHERE estado_civil = 'Casado';",
                            "SELECT COUNT(estado_civil) AS total_solteros FROM public.\"Ciudadanos\" WHERE estado_civil = 'Divorciado';",
                            "SELECT COUNT(*) AS total_defunciones FROM public.\"Defunciones\";",
                            "SELECT COUNT(*) AS total_matrimonios FROM public.\"Matrimonios\";",
                            "SELECT COUNT(*) AS total_divorcios FROM public.\"Divorcios\";"
                         ]
                
                data = []
                # Ejecutar cada consulta
                for query in queries:
                    cur.execute(query)
                    result = cur.fetchone()
                    data.append(result[0])

                if data is not None:
                    return data
                else:
                    print("Data is None")
        except psycopg2.Error as err:
            print("Error al mostrar estadisticas: ", err)
            self.conn.rollback()

    #Cierra la conexion a la BDD al finalizar la ejecucion
    def __del__(self):
        self.conn.close()    