from os import name
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
# Trae el engine de conexión a la base de datos 
from database import engine
from csv import reader

# ----------------------------- CARGADOR TABLA HERRAMIENTAS (tools) ---------------------------------------------
# Leer el archivo csv y convertirlo en una lista de listas
# with open('./CSV_files/Tools.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_tools = list(csv_reader)

# # Ordena la lista de listas de la z-a
# list_of_tools.sort(reverse=True)

# # Motor de encuadre
# metadata = MetaData(engine)

# # Conecta con las tablas de la DB
# tool_table = Table('tools', metadata, autoload=True)

# # Crea un objeto INSERT
# ins = tool_table.insert()

# # Recorre la lista de listas o lista de herramientas e inserta cada una a la DB
# for i in range(len(list_of_tools)):
#     tool=list_of_tools.pop()

#     # Debe tener 4 registros, 1 por cada columna sin contar el id
#     if(len(tool)==4):

#         # Vincula los datos a insertar
#         ins = ins.values(title=tool[0],description=tool[1],image=tool[2],link=tool[3])
        
#         # Hace la conexión
#         conn = engine.connect()

#         # Ejecuta la sentencia Insert
#         conn.execute(ins)
#     else:
#         print("El registro de Herramienta no tiene los campos necesarios, verifique el registro en el archivo .csv")
    
# ----------------------------- CARGADOR TABLA CURSOS (courses) ---------------------------------------------
with open('./CSV_files/Courses.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_courses = list(csv_reader)

list_of_courses.sort(reverse=True)

metadata = MetaData(engine)
course_table = Table('courses', metadata, autoload=True)
ins = course_table.insert()

for i in range(len(list_of_courses)):
    course=list_of_courses.pop()
    if(len(course)==4):
        ins = ins.values(name=course[0],description=course[1],date=course[2],url_course=course[3])
        conn = engine.connect()
        conn.execute(ins)
    else:
        print("El registro de Curso no tiene los campos necesarios, verifique el registro en el archivo .csv")

# ----------------------------- CARGADOR TABLA TALLERES (workshops) ---------------------------------------------
# with open('./CSV_files/Workshops.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_workshops = list(csv_reader)

# list_of_workshops.sort(reverse=True)

# metadata = MetaData(engine)
# workshop_table = Table('workshops', metadata, autoload=True)
# ins = workshop_table.insert()

# for i in range(len(list_of_workshops)):
#     workshop=list_of_workshops.pop()

#     if(len(workshop)==4):
#         ins = ins.values(name=workshop[0],description=workshop[1],date=workshop[2],url_workshop=workshop[3])
#         conn = engine.connect()
#         conn.execute(ins)
#     else:
#         print("El registro de Taller no tiene los campos necesarios, verifique el registro en el archivo .csv")

