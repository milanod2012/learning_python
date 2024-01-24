#number = 124

#this app detemine wich of this values are even or odd
# positive even, negative even, positive odd, negative odd
number = int(input('ingrese valor: '))
# nested if
if number > 0:
    if number % 2  == 0:
        print(f"{number} is even +.") 
    else:
        print(f"{number} is odd + .")
elif number < 0:
    if number % 2  == 0:
        print(f"{number} is even -.") 
    else:
        print(f"{number} is odd - .")
else:
  print("number cero (0)")