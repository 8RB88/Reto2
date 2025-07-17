
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Cargar modelo de embeddings
modelo = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

# Cargar archivos Excel
utpl = pd.read_excel("Carreras_UTPL.xlsx")
unemi = pd.read_excel("Carreras_UNEMI.xlsx")

# Función para limpiar texto
def limpiar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).upper()
    return texto.strip()

# Limpiar columnas relevantes
for col in ['CARRERA_NOMBRE', 'ASIGNATURA_NOMBRE', 'PERIODO_CICLO']:
    utpl[col] = utpl[col].apply(limpiar_texto)
    unemi[col] = unemi[col].apply(limpiar_texto)

# Inicializar resultados
resultados = []

# Recorrer cada materia de UTPL
for i, fila_utpl in utpl.iterrows():
    nivel = fila_utpl['PERIODO_CICLO']
    materia_utpl = fila_utpl['ASIGNATURA_NOMBRE']
    carrera_utpl = fila_utpl['CARRERA_NOMBRE']

    # Filtrar materias UNEMI del mismo ciclo
    subset_unemi = unemi[unemi['PERIODO_CICLO'] == nivel].copy()
    if subset_unemi.empty:
        continue

    # Embeddings de materia UTPL
    emb_utpl = modelo.encode([materia_utpl], convert_to_tensor=True)
    emb_unemi = modelo.encode(subset_unemi['ASIGNATURA_NOMBRE'].tolist(), convert_to_tensor=True)

    # Calcular todas las similitudes
    similitudes = util.cos_sim(emb_utpl, emb_unemi)[0]

    for idx in range(len(subset_unemi)):
        fila_unemi = subset_unemi.iloc[idx]
        score = similitudes[idx].item()
        resultados.append({
            "Carrera_UTPL": carrera_utpl,
            "Materia_UTPL": materia_utpl,
            "Nivel_UTPL": nivel,
            "Carrera_UNEMI": fila_unemi['CARRERA_NOMBRE'],
            "Materia_UNEMI": fila_unemi['ASIGNATURA_NOMBRE'],
            "Nivel_UNEMI": fila_unemi['PERIODO_CICLO'],
            "Score_Similaridad": round(score, 4)
        })

# Guardar resultados completos
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel("resultado_completo_por_nivel.xlsx", index=False)
print("✅ Comparación por nivel completada. Todos los scores guardados.")
