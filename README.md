# Reto 2 - Homologación de Asignaturas con IA

Este proyecto fue desarrollado como parte del Prácticum 2.2 de la Universidad Técnica Particular de Loja (UTPL), y busca facilitar el proceso de homologación de materias entre instituciones de educación superior mediante inteligencia artificial.

## 📌 Descripción del Reto

La UTPL busca fortalecer su estrategia de atracción y homologación de estudiantes provenientes de otras universidades. Para ello, se propone una solución basada en IA que permite comparar mallas curriculares y evaluar si a un estudiante le conviene cambiarse de universidad sin perder materias cursadas.

## ✅ Solución Propuesta

El sistema analiza y compara las mallas curriculares de distintas universidades usando IA para calcular un **score de similitud** entre asignaturas. Esta información alimenta un modelo conversacional (GPT), que puede informar al usuario sobre qué materias pueden homologarse y en qué ciclo académico se ubicaría.

## 💻 Tecnologías Utilizadas

- **Lenguaje de programación:** Python 3
- **Librerías:** `pandas`, `sentence_transformers`
- **Base de datos:** MySQL
- **Fuente de datos:** Mallas curriculares de la UNEMI (formato Excel)

## 🔎 Proceso de Extracción de Datos

Se utilizó ChatGPT para extraer la información desde PDFs e imágenes de las mallas curriculares, estandarizando el formato de salida. Este proceso se aplicó tanto a la UTPL como a la UNEMI, generando cinco archivos Excel por universidad. Finalmente, se consolidaron en un único archivo para su análisis.

## 📊 Análisis de Datos

Se empleó la librería `sentence_transformers` para analizar sintácticamente las asignaturas y calcular un score de similitud. Se trabajó con las siguientes columnas clave:

- `PERIODO_CICLO`
- `ASIGNATURA_NOMBRE`
- `CARRERA_NOMBRE`

Esto permitió medir la similitud entre materias, considerando también el ciclo académico en que se cursan.

## 🗃️ Base de Datos

La base de datos fue normalizada con ayuda de ChatGPT, a partir del Excel final. Se implementó en **MySQL**, creando una estructura relacional adecuada para gestionar las asignaturas, carreras y universidades.

Los datos fueron insertados automáticamente usando un script en Python.

## 🔗 Enlaces Relevantes

- 🔗 Repositorio GitHub: [https://github.com/8RB88/Reto2](https://github.com/8RB88/Reto2)
- 📄 Administración de Empresas UNEMI: [PDF](https://www.unemi.edu.ec/wp-content/uploads/2021/08/MALLA-ADM-EMPRESAS-40-ASIGNATURAS.pdf)
- 📄 Derecho UNEMI: [PDF](https://www.unemi.edu.ec/wp-content/uploads/2024/06/Malla-Derecho-Actualizada-1.pdf)
- 📄 Contabilidad y Auditoría UNEMI: [PDF](https://www.unemi.edu.ec/wp-content/uploads/2021/03/FACSECYD-MALLA-CURRICULAR-CONTABILIDAD-Y-AUDITORIA-2019.pdf)
- 📄 Educación Básica UNEMI: [PDF](https://www.unemi.edu.ec/wp-content/uploads/2025/05/MALLA-EDUCACION-BASICA-EN-LINEA.pdf)
- 📄 Psicología Clínica UNEMI: [PDF](https://www.unemi.edu.ec/wp-content/uploads/2025/06/MALLA-PSICOLOGIA-CLINICA-APROBADA-2025-.pdf)

## 📌 Conclusiones

Este proyecto facilita la toma de decisiones estratégicas en procesos de homologación de asignaturas. Gracias al análisis semántico, se puede identificar similitudes incluso cuando las materias tienen nombres distintos, ayudando tanto a instituciones como a estudiantes.

## 📚 Bibliografía

- Mallas curriculares UNEMI (Excel)
- Documentación oficial de `sentence_transformers` y `pandas`
- Manual de usuario de MySQL
