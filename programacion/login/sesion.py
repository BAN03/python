with open('usuarios.txt', 'r') as file:
    nuser = file.readlines()
with open('usuarios.txt', 'r') as file:
    usuarios = file.read()
user = input('Nombre del usuario: ')
pwd = input("Ingresa la contraseña: ")

index = 0
for linea in usuarios.split('\n'):
    usr_index = linea.split(':')
    if usr_index[0] == user:
        if usr_index[1] == pwd:
            print('sesion iniciada')
            nuser[index] = user + ":" + input('Nueva contraseña: ') + '\n'
            with open('usuarios.txt', 'w') as file:
                file.writelines(nuser)

    index += 1
