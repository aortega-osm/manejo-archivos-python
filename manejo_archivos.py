try:
    archivo = open("prueba.txt","w")
    archivo.write("HOLA MUNDO\n")
    archivo.write("Texto\n")
    archivo.write("Adios\n")
except Exception as e:
    print(e)
finally:
    archivo.close()
    # archivo.write("Hola")