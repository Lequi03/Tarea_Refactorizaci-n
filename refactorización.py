def primera_opcion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        puntuacion = input()
                
        if puntuacion.isdecimal():
            puntuacion = int(puntuacion)
                    
            if puntuacion <= 0 or puntuacion > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                 print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comentario = input()
                post = f'punto: {puntuacion} comentario: {comentario}'
                with open("data.txt", "a") as archivo_pc:
                    archivo_pc.write(f'{ post } \n')
                    archivo_pc.close()
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def segunda_opcion():
    print('Resultados hasta la fecha.')
    leer_archivo = open("data.txt", "r")
    print(leer_archivo.read())
    leer_archivo.close()
        
while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()
    if num.isdecimal():
        num = int(num)
        if num == 1:   
           primera_opcion() 
        elif num == 2:
            segunda_opcion()
        elif num == 3:
            print('Finalizando')
            break  # Sentencia para finalizar el procesamiento
        
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')