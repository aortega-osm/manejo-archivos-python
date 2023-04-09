#archivo = open("c:\\Users\\Alexo\\Documents\\Proyecto\\manejo-archivos-python\\prueba.txt", "r+" encording="utf8")
archivo = open("prueba.txt", "r",encoding="utf8")
# print(archivo.read())

#  leer algunos caracteres
# print(archivo.read(2))
# print(archivo.read(3))

#  leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#  print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[2])

# abrimos un nuevo archivo
# a- anexar informacion
archivo2=open("copia.txt", "a")
archivo2.write(archivo.read())

archivo2.close()
archivo.close()
print("Se ha terminado la lectura")
