# with open("prueba.txt", "r", encoding="utf8") as archivo:
from manejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())

