import pandas as pd

# Leer los datos del archivo Excel
usuariosDataFrame = pd.read_excel("./Data/usuarios_sistema_completo.xlsx")

# Asegurar que la columna de fecha sea tipo datetime
usuariosDataFrame['fecha_nacimiento'] = pd.to_datetime(usuariosDataFrame['fecha_nacimiento'], errors='coerce')

# Revisar valores nulos
print("Valores nulos por columna:")
print(usuariosDataFrame.isnull().sum())

# Listado solo de aprendices
print("Aprendices:")
print(usuariosDataFrame.query('tipo_usuario == "aprendiz"'))

# Listado de instructores o docentes
print("Docentes:")
print(usuariosDataFrame.query('tipo_usuario == "docente"'))

# Profesores especializados en Ingeniería de Sistemas
print("Docentes especializados en Ingeniería de Sistemas:")
print(usuariosDataFrame[usuariosDataFrame['especialidad'].isin(['Ingenieria de Sistemas'])])


# Cargar los datos
df = pd.read_excel("./Data/usuarios_sistema_completo.xlsx")

# Convertir la columna de fecha a tipo datetime
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

# Usuarios con dirección en Medellín
print("Usuarios con dirección en Medellín:")
print(df[df['direccion'].str.contains("medellin|med", case=False, na=False)])

# Usuarios cuya dirección termina en 'sur'
print("Usuarios cuya dirección termina en 'sur':")
print(df[df['direccion'].str.strip().str.endswith("sur", na=False)])

# Docentes con 'datos' en la especialidad
print("Docentes con 'datos' en la especialidad:")
print(df[df['especialidad'].str.contains("datos", case=False, na=False)])

# Usuarios nacidos en o antes de 1990
print("Usuarios nacidos en o antes de 1990:")
print(df[df['fecha_nacimiento'].dt.year <= 1990])

# Docentes mayores (nacidos en o antes de 1975)
print("Docentes mayores (nacidos en o antes de 1975):")
print(df[(df['fecha_nacimiento'].dt.year <= 1975) & (df['tipo_usuario'] == "docente")])

# Profesores y aprendices nacidos en o después del 2000
print("Profesores y aprendices nacidos en o después del 2000:")
print(df[(df['fecha_nacimiento'].dt.year >= 2000) & (df['tipo_usuario'].isin(["docente", "estudiante"]))])