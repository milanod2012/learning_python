# inicializar las variables
product_list = []
product = ''
#
# while product != 'echo':
while True:  # hace lo mismo el codigo de arriba
             # 
    product = input("Enter a product name or type 'echo' to display the list: ")
    
    if product == 'echo': # hace un break en echo omitiendo al imprimir la lista  
        break

    product_list.append(product)
print("\n Lista de Productos")
for index, value in enumerate(product_list, start=1):
    print(f"{index}. {value}")