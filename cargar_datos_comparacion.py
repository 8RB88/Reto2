
import pandas as pd
import mysql.connector

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="peluza",
    database="comparacion_carreras"
)
cursor = conn.cursor()

# Cargar el archivo Excel
df = pd.read_excel("resultado_completo_por_nivel.xlsx")

# Insertar universidades
cursor.execute("INSERT IGNORE INTO universidad (nombre) VALUES ('UTPL')")
cursor.execute("INSERT IGNORE INTO universidad (nombre) VALUES ('UNEMI')")
conn.commit()

# Obtener IDs de universidades
cursor.execute("SELECT id FROM universidad WHERE nombre='UTPL'")
utpl_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM universidad WHERE nombre='UNEMI'")
unemi_id = cursor.fetchone()[0]

# Diccionarios auxiliares para evitar duplicados
carreras = {}
materias = {}

# Función para obtener o insertar carrera
def get_or_create_carrera(nombre, universidad_id):
    clave = (nombre, universidad_id)
    if clave in carreras:
        return carreras[clave]
    cursor.execute("SELECT id FROM carrera WHERE nombre=%s AND universidad_id=%s", (nombre, universidad_id))
    result = cursor.fetchone()
    if result:
        carreras[clave] = result[0]
    else:
        cursor.execute("INSERT INTO carrera (nombre, universidad_id) VALUES (%s, %s)", (nombre, universidad_id))
        conn.commit()
        carreras[clave] = cursor.lastrowid
    return carreras[clave]

# Función para obtener o insertar materia
def get_or_create_materia(nombre, nivel, carrera_id):
    clave = (nombre, nivel, carrera_id)
    if clave in materias:
        return materias[clave]
    cursor.execute("SELECT id FROM materia WHERE nombre=%s AND nivel=%s AND carrera_id=%s", (nombre, str(nivel), carrera_id))
    result = cursor.fetchone()
    if result:
        materias[clave] = result[0]
    else:
        cursor.execute("INSERT INTO materia (nombre, nivel, carrera_id) VALUES (%s, %s, %s)", (nombre, str(nivel), carrera_id))
        conn.commit()
        materias[clave] = cursor.lastrowid
    return materias[clave]

# Insertar datos
for _, row in df.iterrows():
    c_utpl = get_or_create_carrera(row['Carrera_UTPL'], utpl_id)
    c_unemi = get_or_create_carrera(row['Carrera_UNEMI'], unemi_id)
    m_utpl = get_or_create_materia(row['Materia_UTPL'], row['Nivel_UTPL'], c_utpl)
    m_unemi = get_or_create_materia(row['Materia_UNEMI'], row['Nivel_UNEMI'], c_unemi)

    cursor.execute("""
        INSERT INTO comparacion_materias (materia_utpl_id, materia_unemi_id, score_similaridad)
        VALUES (%s, %s, %s)
    """, (m_utpl, m_unemi, row['Score_Similaridad']))

conn.commit()
cursor.close()
conn.close()
print("✅ Datos cargados exitosamente en MySQL.")
