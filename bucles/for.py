# inicializar las variables
product_list = []
product = ''
#
while product != 'echo':
    product = input("Enter a product name or type 'echo' to display the list: ")


    product_list.append(product)

print("\n Lista de Productos")

counter = 1
for value in product_list:
    print(f"{counter}. {value}")
    counter +=1
   
