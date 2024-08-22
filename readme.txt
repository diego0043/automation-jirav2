Lo primero que se debe realizar es crear un API KEY de Jira en la siguiente página: 
https://id.atlassian.com/manage/api-tokens

Una vez creado el API KEY, se debe crear un archivo .env en la carpeta scripts del proyecto con la siguiente estructura:
- Nombre del archivo: private_credentials.py

- Dentro de este agregar las siguientes variables ( omitir el * ):
  * from config import HTTPBasicAuth

  * jira_url = "https://siman.atlassian.net/"
  * api_endpoint = f"{jira_url}/rest/api/2/issue"
  * token = "" ( Aqui va el token generado en la página de Jira)
  * auth = HTTPBasicAuth("correo@siman.com", token) ( Aqui va el correo con el que se generó el token )
  * project_key = "" ( Aqui va el key del proyecto de Jira ejemplo: "ADCK" )

para instalar las dependencias necesarias para correr el proyecto, ejecutar el siguiente comando en la terminal estando dentro de la carpeta del proyecto:
>>pip install -r requirements.txt

para correr el proyecto estando dentro de la carpeta, ejecutar el siguiente comando en la terminal:
>>python scripts/main.py
