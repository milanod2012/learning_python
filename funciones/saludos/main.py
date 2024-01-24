import saludos

message = saludos.hello("name")
print(message)


messages = saludos.hellos("uno", "dos", "tres")
for message in messages.values():
    print(message)
