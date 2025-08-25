try:
    x = 10 / 2
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("División exitosa, el resultado es:", x)
finally:
    print("Este bloque siempre se ejecuta.")