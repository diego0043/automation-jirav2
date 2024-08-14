from config import *
from private_credentials import *

def create_task_backlog(name_task, priority, type, num_subtask = 0):
    try:
    # Datos del issue a crear
        issue_data = {
            "fields": {
                "project": {
                    "key": "CSC"  # Reemplaza con la clave del proyecto
                },
                "summary": name_task,  # Título del issue
                "description": "Descripción detallada de la tarea",
                "issuetype": {
                    "name": type  # Cambia esto a "Bug", "Story", etc. si es necesario
                },
                "priority": {
                    "name": priority  # Configura la prioridad (High, Medium, Low, etc.)
                },
            }
        }

        # Solicitud para crear el issue
        response = requests.post(api_endpoint, 
                                headers={"Content-Type": "application/json"}, 
                                auth=auth, 
                                data=json.dumps(issue_data))

        # Comprobar si la creación fue exitosa
        if response.status_code == 201:
            issue_key = response.json()["key"]

            # Crear subtareas
            if num_subtask > 0:

                template_subtask = "DEV - " +str(name_task) if type == "Task" else "QA - Ejecución de pruebas - "+str(name_task)
                for k in range(num_subtask):
                    subtask_data = {
                        "fields": {
                            "project": {
                                "key": "CSC"
                            },
                            "summary": template_subtask,
                            "parent": {
                                "key": issue_key
                            },
                            "issuetype": {
                                "name": "Sub-task"
                            },
                            "priority": {
                                "name": priority  # Configura la prioridad (High, Medium, Low, etc.)
                            },
                        }
                    }

                    response = requests.post(api_endpoint, 
                                            headers={"Content-Type": "application/json"}, 
                                            auth=auth, 
                                            data=json.dumps(subtask_data))

                    if response.status_code != 201:
                        print(f"Algo salió mal creando la subtarea {k+1}: {response.status_code} {response.text}")

            print(f"Issue creado correctamente: {issue_key}")
        else:
            print(f"Error creando el issue: {response.status_code} {response.text}")
    
    except Exception as e:
        print(f"Error creando el issue: {e}")