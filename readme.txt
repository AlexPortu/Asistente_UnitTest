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

Cada test es una función que empieza por "test_"... dentro de testcase/<test_...>.py. Se configura un test por cada swimlane y el objetivo es llegar a formalizar un carrito de compra con los inputs que el usuario ofrece al principio de cada test. El test se dará por válido si ha llegado a finalizar todo el proceso

Para ejecutar los tests:
    python testcase/<Nombre del archivo>
    ejemplo: python testcase/test_forfait.py


Como está configurado un test:

Todo test sigue una misma estructura. Primero empiza inicializando el test con una función llamada SetUp(). A continuación le sigue una función propia del test. En cada caso y según la swimlane, se seguirá una camino de test diferente. Por último, se finaliza el test con la funcion TearDown().

Estructura del proyecto:

    1. test_<swimlane>.py configuran los propios tests. Utilizan clases de los archivos a continuación.
    2. page.py almacena las funciones y variables de los elementos de la web de asistentes. Por ejemplo, el boton continuar se almacena en una clase referente a la página donde se encuentra. Los elementos se denominan con el_<nombre_del_elemento>. Pueden ser funciones o variables.
    3. locator.py guarda la información html de cómo encontrar los elementos que se hacen referencia page.py. Esto es para hacer el código más limpio y tenerlo todo bien organizado.
    4. selectorvalues.py almacena información semi-estática en donde el usuario va a poder consultar las opciones disponbiles cuando el test le exija parámtros obligatorios para realizar el proceso.



