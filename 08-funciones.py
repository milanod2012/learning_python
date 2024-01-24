#funcion con return y parametro 
def saludar(nombre):
    return f'hola,{nombre}' 'funcion saludar'

def sumar(a,b):
    return a+b

def restar(a=None,b=None):
    if a== None or b== None:
        print('los valores de a y b estan vacios')
        return
    return a-b





saludo= saludar('daniel ')
print(saludo)
print('-'*40) #espacio

suma=sumar(10,20)
print("la suma de ",  'es', suma )
print('-'*40) #espacio

resta= restar(b=20, a=40)
print('la resta es ', resta)
resta= restar()
print('la resta es ', resta)
