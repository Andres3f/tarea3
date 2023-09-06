telefono = input("Introduce un número de teléfono con el formato prefijo-número-extensión: ")
partes = telefono.split("-")
numero = partes[1]

print(f"El número de teléfono sin el prefijo y la extensión es: {numero}")