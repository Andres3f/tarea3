email = input("Introduce tu correo electrónico: ")
nombre, dominio = email.split('@')
nuevo_email = nombre + '@ceu.es'
print("Tu nuevo correo electrónico es:", nuevo_email)
