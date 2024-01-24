#imprimir fecha de hoy

from datetime import date
print("la fecha de hoy es: " + str(date.today()))

#programa para el calculo de venta
#:.2f formatea el valor con dos decimales por ejemplo 100.00

venta= int(input("ingrese el valor de venta"))
impuesto= venta * 0.18
calculo = venta + impuesto
print(f'base {venta:.2f}\nimpuestos {impuesto:.2f}\ntotal a cancelar {calculo:.2f}')





