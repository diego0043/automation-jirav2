from config import *
from methods import *

#prioridades:
#Highest (Más alta), High (Alta), Medium (Media), #Low (Baja), #Lowest (Más baja)

# Ejemplo de como se deben crear el arreglo de datos para crear tareas y subtareas
data = [
    ["Test 2", "Highest", "Task", 2],
]

# Ejemplo de como se deben crear el arreglo de datos para crear subtareas dentro de una tarea ya existente
data2 = [
    ["ADCK-234", "Test creacion automatica-2", "Lowest", "Story", 2],

]

# método para crear subtareas: create_subTask(parent, name_task, priority, type, num_subtask)
# método para crear tareas y subtareas: create_task_backlog(name_task, priority, type, num_subtask)

# Iterar sobre los datos y crear las tareas y subtareas Jira
for d in data2:
    create_subTask(d[0], d[1], d[2], d[3], d[4])
    #create_subTask(d[0], d[1], d[2], d[3], d[4])



