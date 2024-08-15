from config import *
from methods import *

#prioridades:
#Highest (Más alta), High (Alta), Medium (Media), #Low (Baja), #Lowest (Más baja)

# Ejemplo de como se deben crear el arreglo de datos para crear tareas y subtareas
data = [
    ["Tareas inter sprint", "Lowest", "Sub-task", 5],
    ["Tareas de desarrollo", "Low", "Sub-task", 5],
    ["Tareas de QA", "Low", "Sub-task", 5],
]

# Ejemplo de como se deben crear el arreglo de datos para crear subtareas dentro de una tarea ya existente
data2 = [
    ["CSC-403", "Tarea existente", "Lowest", "Task", 5],
    ["CSC-404", "Tarea existente", "Low", "Task", 5],
    ["CSC-405", "Tarea existente", "Low", "Task", 5],
]

# método para crear subtareas: create_subTask(parent, name_task, priority, type, num_subtask)
# método para crear tareas y subtareas: create_task_backlog(name_task, priority, type, num_subtask)

# Iterar sobre los datos y crear las tareas y subtareas Jira
for d in data:
    create_task_backlog(d[0], d[1], d[2], d[3])



