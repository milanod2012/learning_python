# inicializar las variables
product_list = []
product = ''
#
while product != 'echo':
    product = input("Enter a product name or type 'echo' to display the list: ")


    product_list.append(product)
print("\n Lista de Productos")
counter = 1
index = 0
while index < len(product_list):
    print(f"{counter}. {product_list[index]}")
    counter +=1
    index +=1
