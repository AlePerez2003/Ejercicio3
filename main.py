from registro import Registro
from manejador_meteorologo import Meteorología
import csv

if __name__ == '__main__':
    registros = Meteorología()
    registros.leer_archivo()
    registros.menu()
    