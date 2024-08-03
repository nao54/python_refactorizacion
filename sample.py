def ingresar_puntuacion_comentario():
    while True:
        try:
            point = int(input('Ingrese una puntuación del 1 al 5: '))
            if 1 <= point <= 5:
                comment = input('Ingrese un comentario: ')
                post = f'Puntuación: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Por favor, introduzca un valor entre el 1 y 5.')
        except ValueError:
            print('Por favor, introduzca un valor numérico para la puntuación.')

def revisar_resultados():
    print('Resultados hasta ahora:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados.strip(): 
                print(resultados)
            else:
                print('No hay resultados aún.')
    except FileNotFoundError:
        print('No hay resultados aún (archivo no encontrado).')
    except IOError as e:
        print(f'Error al leer el archivo: {e}')

def seleccionar_proceso():
    while True:
        print('Seleccione la operación que desea realizar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Revisar resultados')
        print('3: Salir')
        try:
            num = int(input())
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                revisar_resultados()
            elif num == 3:
                print('Saliendo...')
                break
            else:
                print('Por favor, introduzca un valor entre el 1 y 3.')
        except ValueError:
            print('Por favor, introduzca un valor entre el 1 y 3.')

if __name__ == "__main__":
    seleccionar_proceso()








