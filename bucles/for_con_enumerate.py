# inicializar las variables
product_list = []
product = ''
#
while product != 'echo':
    product = input("Enter a product name or type 'echo' to display the list: ")


    product_list.append(product)

print("\n Lista de Productos")

for index, value in enumerate(product_list, start=1):
    print(f"{index}. {value}")
