for i in range(10):
    if i == 5:
        break # this wil end at number 4 because is counting from 0
    print(i)  # This will be printed 10 times.

print("-"*20)

for i in range(5):
    if i == 2:
        continue   #this wil forget a number 2
    print(i)