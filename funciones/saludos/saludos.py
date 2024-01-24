import random
from typing import Dict

def randon_formats() -> str:   
   #lista de saludos
    formats = [
        "hi, {}! welcome", 
        "nice to see you {}",   
        "greetings {}! nice to know you!" 
    ]

#seleccionar un elemento aleatorio de la lista
    return random.choice(formats)


def hello(name):
    if name == '':
        return f"nombre vacio. "


    message = randon_formats().format(name)
    return message

def hellos(*names:str) -> Dict[str,str]:
    messages = {}

    for name in names:
        message = hello(name)
        messages[name] = message
    return messages

