frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

vocal_mayuscula = vocal.upper()
frase_modificada = frase.replace(vocal, vocal_mayuscula)

print("La frase modificada es:", frase_modificada)
