# quiz_empresas.py
# Quiz 1 - Fundamentos de programacion (Programacion Estructurada + POO)
# Tu tarea: completar todos los bloques marcados con "# TODO".
# Cada linea de empresas.txt tiene:  nombre, sector, num_empleados, ingresos_anuales
# Para ejecutar:  python quiz_empresas.py
#
# CONSEJO: ve completando un TODO a la vez y ejecuta el archivo para ver como
#          se va llenando la salida. Al inicio veras resultados vacios o en cero.


# 1) LA CLASE: representa UNA empresa (datos + comportamiento juntos)
class Empresa:
    """Representa UNA empresa: encapsula sus datos y su comportamiento."""

    # El CONSTRUCTOR se ejecuta al crear el objeto y guarda sus datos.
    # 'self' es el propio objeto que se esta construyendo.
    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        # Guarda cada parametro como un atributo del objeto.
        # Convierte num_empleados e ingresos_anuales a numero con int().
        self.nombre = nombre
        self.sector = sector
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)

    def obtener_informacion(self):
        """Devuelve los datos de la empresa como un texto legible."""
        # Usa un f-string con los atributos de self.
        return (
            f"{self.nombre} | {self.sector} | "
            f"{self.num_empleados} empleados | ${self.ingresos_anuales}"
        )

# 2) Leer el archivo y crear una LISTA DE OBJETOS Empresa
def leer_empresas(nombre_archivo):
    """Lee el archivo y crea un objeto Empresa por cada linea valida.

    Una linea es INVALIDA si num_empleados es menor o igual a 0:
    en ese caso NO se crea el objeto (se ignora el registro).
    """
    empresas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")
            # Solo crea y agrega la empresa si tiene empleados mayores a 0.
            if int(num_empleados) > 0:
                empresa = Empresa(
                    nombre, sector, num_empleados, ingresos_anuales
                )
                empresas.append(empresa)
    return empresas

# 3) Sumar los ingresos de todas las empresas
def calcular_total_ingresos(empresas):
    """Devuelve la suma de los ingresos_anuales de todas las empresas."""
    # Recorre la lista y suma los ingresos de cada empresa.
    total = 0
    for empresa in empresas:
        total += empresa.ingresos_anuales
    return total

# 4) Quedarse solo con las empresas de un sector
def filtrar_por_sector(empresas, sector):
    """Devuelve una lista con las empresas cuyo sector coincide."""
    # Devuelve una lista solo con las empresas del sector indicado.
    return [empresa for empresa in empresas if empresa.sector == sector]

# 5) Encontrar la empresa con mas empleados
def empresa_con_mas_empleados(empresas):
    """Devuelve el objeto Empresa que tiene mas empleados."""
    # Revisa si la lista está vacía.
    if not empresas:
        return None

    # Supone que la primera empresa tiene más empleados.
    mayor = empresas[0]

    # Compara las demás empresas para encontrar la que tiene más empleados.
    for empresa in empresas[1:]:
        if empresa.num_empleados > mayor.num_empleados:
            mayor = empresa

    return mayor

# 6) Calcular el promedio de empleados
def promedio_empleados(empresas):
    """Devuelve el promedio de empleados de todas las empresas."""
    # Si la lista está vacía, devuelve 0 para evitar dividir entre cero.
    if not empresas:
        return 0

    # Suma los empleados y divide entre la cantidad de empresas.
    total_empleados = sum(empresa.num_empleados for empresa in empresas)
    return total_empleados / len(empresas)

# 7) Funcion principal: usa todo lo anterior y muestra los resultados
def ejecutar_quiz():
    empresas = leer_empresas("empresas.txt")

    print("--- Empresas registradas ---")
    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")
    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)
    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))


# Iniciar el programa
ejecutar_quiz()