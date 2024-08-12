para poder ejecutar el proyecto se necesita descargar el archivo de la siguiente dirección:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads

una vez descargado el archivo, se debe descomprimir y guardar en una carpeta en el disco local, por ejemplo en la carpeta C:\webdrivers

Luego se debe agregar el path en el archivo de configuración del proyecto, en el archivo config_selenium.py, en la variable path_driver, por ejemplo:
path_driver = 'C:/webdrivers/msedgedriver.exe'

para instalar las dependencias necesarias para correr el proyecto, ejecutar el siguiente comando en la terminal estando dentro de la carpeta del proyecto:
>>pip install -r requirements.txt

para correr el proyecto, ejecutar el siguiente comando en la terminal:
>>python main.py
