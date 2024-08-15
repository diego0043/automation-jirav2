from config import *
from methods import *

#prioridades:
#Highest (Más alta), High (Alta), Medium (Media), #Low (Baja), #Lowest (Más baja)

# Ejemplo de como se deben crear el arreglo de datos para las tareas
data = [
    ["Tareas inter sprint", "Lowest", "Sub-task", 5],
    ["Tareas de desarrollo", "Low", "Sub-task", 5],
    ["Tareas de QA", "Low", "Sub-task", 5],
]

# Iterar sobre los datos y crear las tareas en Jira
for d in data:
    create_subTask(d[0], d[1], d[2], d[3], d[4])



