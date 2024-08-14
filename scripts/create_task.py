from config import *
from methods import *

#Highest (Más alta), High (Alta), Medium (Media), #Low (Baja), #Lowest (Más baja)

data = [
    ["CSC-4268", "Tareas inter sprint", "Lowest", "Sub-task", 5],
    
]

for d in data:
    create_subTask(d[0], d[1], d[2], d[3], d[4])



