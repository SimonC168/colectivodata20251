import pandas as pd

# Leer los datos de asistencia
asistenciaDataFrame = pd.read_csv("./Data/asistencia_estudiantes_completo.csv")

# Convertir la columna 'fecha' a tipo datetime
asistenciaDataFrame['fecha'] = pd.to_datetime(asistenciaDataFrame['fecha'])

# Información general del DataFrame (opcional para análisis exploratorio)
# print(asistenciaDataFrame.head(10))
# print(asistenciaDataFrame.tail(10))
# print(asistenciaDataFrame.info())
# print(asistenciaDataFrame.describe())
# print(asistenciaDataFrame.isnull().sum())
# print(asistenciaDataFrame['estado'].value_counts())
# print(asistenciaDataFrame['estrato'].value_counts())

# ------------------- Consultas -------------------

estudiantes_que_asistieron = asistenciaDataFrame.query('estado == "asistio"')
estudiantes_que_no_asistieron = asistenciaDataFrame.query('estado == "inasistencia"')
estudiantes_que_justificaron = asistenciaDataFrame.query('estado == "justificado"')

estudiantes_estrato_1 = asistenciaDataFrame.query('estrato == 1')
estudiantes_estrato_alto = asistenciaDataFrame.query('estrato == 5 or estrato == 6')

estudiantes_en_metro = asistenciaDataFrame.query('medio_transporte == "metro"')
estudiantes_en_bicicleta = asistenciaDataFrame.query('medio_transporte == "bicicleta"')
estudiantes_no_a_pie = asistenciaDataFrame.query('medio_transporte != "a pie"')

# Registros del mes de junio
registros_junio = asistenciaDataFrame[asistenciaDataFrame['fecha'].dt.month == 6]

# Estudiantes que usan transporte ecológico
transportes_ecologicos = ['a pie', 'bicicleta', 'metro', 'bus']
estudiantes_transporte_ecologico = asistenciaDataFrame[asistenciaDataFrame['medio_transporte'].isin(transportes_ecologicos)]

# Transporte vs estrato
estrato_alto_en_bus = asistenciaDataFrame.query('medio_transporte == "bus" and estrato >= 5')
estrato_bajo_en_bus = asistenciaDataFrame.query('medio_transporte == "bus" and estrato <= 2')
estrato_alto_caminando = asistenciaDataFrame.query('medio_transporte == "a pie" and estrato >= 5')
estrato_bajo_caminando = asistenciaDataFrame.query('medio_transporte == "a pie" and estrato <= 2')

# ------------------- Estadísticas -------------------

#conteo_asistencia = asistenciaDataFrame['estado'].value_counts()conteo_por_estrato = asistenciaDataFrame['estrato'].value_counts()
conteo_por_transporte = asistenciaDataFrame['medio_transporte'].value_counts()

promedio_estrato_por_estado = asistenciaDataFrame.groupby('estado')['estrato'].mean()
max_estrato_por_estado = asistenciaDataFrame.groupby('estado')['estrato'].max()
min_estrato_por_estado = asistenciaDataFrame.groupby('estado')['estrato'].min()

conteo_grupo_estado = asistenciaDataFrame.groupby(['id_grupo', 'estado']).size()