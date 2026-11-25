Cada archivo .py tiene su propia etiqueta __name__ privada. Python solo tiene dos reglas para llenar esa etiqueta:

Si TÚ abres ese archivo directamente desde la terminal (ejemplo: escribes py app.py y das Enter):
Python dice: "Este es el jefe del programa", y le pone la etiqueta '__main__'. (No importa que este archivo importe otros o no importe ninguno; como tú lo arrancaste directamente, su etiqueta es '__main__').

Si otro archivo lo manda llamar con import (ejemplo: adentro de app.py pones import hola):
Python dice: "Este archivo hola.py no es el jefe, solo vino a ayudar", y le pone como etiqueta su nombre real de archivo: 'hola'.