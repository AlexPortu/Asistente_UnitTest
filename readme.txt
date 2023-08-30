Unit Test de las diferentes swimlanes de assistant.grandvalira.com/intereses


Instalaciones

    1. Clonar el repositorio
    2. Instalar driver de google chrome con la versión actual de chrome en el equipo.
    3. Crear un Entorno Virtual donde instalar requirements.txt


1. Para clonar el repositorio abrir una terminal de comando y pegar: 

    git clone https://github.com/AlexPortu/Asistente_UnitTest.git

2. Los drivers de Google Chrome se encuentran en este link: https://chromedriver.chromium.org/downloads
Atención: Es importante que el driver sea versión "116.0.5845.96" o superior. Una vez descargado el driver, ubicar el archivo .exe en el mismo directorio donde tenga ubicado el repositorio.

3. Para hacer uso de este webdriver lo que mejor me ha funcionado ha sido la consola de Powershell. Para ello los comandos necesarios están adaptados a dicha terminal:

Crear virtual environment:
    python -m venv venv

Activar venv:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
    venv\Scripts\activate.ps1

Instalar los requerimientos:
    pip install -r requirements.txt


Como executar los tests:

Cada test es una función que empieza por "test_"... dentro de testcase/main.py. Se configura un test por cada swimlane y el objetivo es llegar a formalizar un carrito de compra con los inputs que el usuario ofrece al principio de cada test. El test se dará por válido si ha llegado a finalizar todo el proceso

Para ejecutar los tests:
    python testcase/main.py

