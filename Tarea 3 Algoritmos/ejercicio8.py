precio = float(input("Introduce el precio del producto en euros con dos decimales: "))
euros = int(precio)
centimos = round((precio - euros) * 100)
print("El precio del producto es de {} euros y {} céntimos".format(euros, centimos))
