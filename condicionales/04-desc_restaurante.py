total_amount = float(input("monto de consumo: $"))

#calcular descuento
if total_amount > 50 and total_amount <= 100:
    discount =  0.1 
elif total_amount > 100 and total_amount <= 200:
     discount =  0.2
elif total_amount > 200: 
     discount =  0.3
else:
     discount= 0.0

#calcular monto final con descuento
discount_amount = total_amount * discount 
final_amount = total_amount - discount_amount


#mostrar el resumen de la cuenta

print("resumen de la cuenta")
print("-"*30)
print(f"monto de comsumo: $ {total_amount:.2f}" )
print(f"descuento del {discount*100:.0f}%")
print(f"Monto a pagar: $ {final_amount:.2f}")






