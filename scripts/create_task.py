from config import *
from methods import *

#Highest (Más alta)
#High (Alta)
#Medium (Media)
#Low (Baja)
#Lowest (Más baja) """

data = [
    ["Tareas inter sprint", "Lowest", "Story", 5],
    ["Procesos despliegues UX", "Lowest", "Story", 2],
]

for d in data:
    create_task_backlog(d[0], d[1], d[2], d[3])



