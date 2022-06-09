#####################################################################################################
######################## INTRODUCCION A LA PROGRAMACION #############################################
##############################VALIDACION DE ENTRADA##################################################
#####################################################################################################
#Repositorio: https://github.com/CarlaGonzalezz/trabajos-practicos-unlu.git
#Apellido y nombre: Gonzalez Carla Micaela
#Legajo: 190256
#####################################################################################################

#Hasta el momento asumimos que el usuario, cuando le solicitamos ingresar algún dato
#por teclado, siempre nos provee un valor válido, o en el peor de los casos, podemos
#validar una única vez su entrada. Cuando el valor era inválido, nos limitábamos a
#terminar el programa. Sin embargo, en un contexto real, debemos contemplar la
#posibilidad de que el usuario ingrese datos inválidos más de una vez, y el programa
#debe seguir funcionando. En forma general, validar un dato significa:
#● Verificar que es del tipo correcto. Esto es importante ya que si, por ejemplo,
#intentamos realizar una operación numérica sobre un valor alfanumérico, se
#● Verificar si el valor está dentro del rango permitido. Una vez que sabemos que el
#dato es del tipo correcto, debemos verificar que el valor esté dentro del rango
#que aceptaremos como válido. Por ejemplo, una nota de parcial tiene que ser un
#número entero entre 1 y 10 (el valor 12 sería inválido); o un día de la semana
#debería ser un string y coincidir con el literal “lunes”, “martes”, miércoles”,
#“jueves”, “viernes”, “sábado”, o “domingo” (el valor “osvaldo” sería inválido).
#● Reaccionar a una entrada inválida. Al detectar que el usuario ha ingresado un
#valor inválido, debemos decidir qué hacer. Para el contexto de este trabajo
#práctico, nos valdremos de las estructuras repetitivas para permitir el reingreso
#de los datos.

##########################################################################################
#FUNCIONES QUE DEBE PROGRAMAR.
##########################################################################################


#1. Cree un script que le solicite al usuario ingresar una temperatura en grados
#Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
#temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
#programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
#que el usuario provea un dato válido. Procure informar al usuario cuando su
#dato es inválido, y cuáles son los valores aceptados.



def celsius():
    print("Ingrese la temperatura en grados C°\nEl valor permitido es de entre -18 y 50°.")
    dato = 0
    centinela = True
    while centinela:
        dato = input("Ingrese la temperatura:")
        if dato.isnumeric():
            if int(dato)<=50 and int(dato)>=-18:
                print("Su dato es valido.")
                centinela = False
            else:
                print("Su dato no es valido.")
        else:
            print("Su dato esta fuera del rango permitido, por favor ingrese un dato valido.")
            

#2. Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato
#ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el
#rango válido para este programa es de 18 a 60 años. El programa debe solicitar
#el reingreso de manera indefinida, hasta que el dato sea correcto.

def tu_edad():
    centinela = True
    while centinela:
        edad = input("Ingrese su edad\nEl rango permitido es de 18 a 60 años:")
        if edad.isnumeric():
            if int(edad) <=60 and int(edad) >= 18:
                print("El dato ingresado es valido.")
                centinela  = False
            else:
                print("El dato ingresado no es valido.")
                input("Ingrese nuevamente su edad:")
        else:
            print("El dato ingresado esta fuera del rango permitido, intente nuevamente.")

#3. Modifique todos los ejercicios anteriores para que en lugar de permitir el
#reintento de manera ilimitada, el programa permita sólo 10 reintentos. Si el
#usuario supera el límite de reintentos, el programa debe terminar con el
#mensaje “Usted está jugando conmigo, yo me retiro”.

def grados():
    print("Ingrese la temperatura en grados C°\nEl valor permitido es de entre -18 y 50°.")
    dato = 0
    for i in range(1,10):
        dato = input("Ingrese la temperatura:")
        if dato.isdigit():
            if int(dato)<=50 and int(dato)>=-18:
                print("Su dato es valido.")
                
            else:
                print("Su dato no es valido.")
        else:
            print("Su dato esta fuera del rango permitido, por favor ingrese un dato valido.")
    print("Se le acabaron los intentos, usted esta jugando conmigo.")
 

#4. La técnica de validación para un conjunto específico de valores se puede utilizar
#para construir menús de opciones. Construya un menú que le muestre al
#usuario lo siguiente:
#********* MI PROGRAMA *********
#1. Saludar.
#2. Informar temperatura.
#3. Mostrar nombre de materia.
#4. Salir.
#Seleccione una opción [1-4]:
#- Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola,
#bienvenido a mi programa interactivo!”.
#- Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una
#sensación térmica de 20 grados Celsius.”.
#- Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la
#- materia Introducción a la Programación!”.
#- Cuando el usuario ingrese la opción 4, el programa debe terminar,
#mostrando el mensaje “Hasta la próxima!”.
#- Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
#inválida.”.

import os

def menu():
    print("****MI PROGRAMA****\n 1. Saludar.\n 2. Informar temperatura.\n 3. Mostrar nombre de materia.\n 4. Salir.")
dato = 0
while dato != 4:
    os.system("cls")
    menu()
    dato = int(input("Selecione una opcion [1-4] :"))
    if dato == 1:
        print("Hola, bienvenido a mi programa interactivo!")
    elif dato == 2:
        print("Hay una sensacion termica de 20 grados celsius.")
    elif dato == 3:
        print("Estas en la materia de introduccion a la programacion!")
    elif dato == 4:
        print("Hasta la proxima!")
    else:
        print("Opcion invalida.")

    input("PRESIONE ENTER PARA CONTINUAR.") 


#5. Cree un script que le solicite al usuario ingresar cuál es su color favorito,
#limitando las opciones a rojo, verde, y azul. Aclaraciones:
#- Puede asumir que el usuario ingresará los strings en minúsculas.
#Opcionalmente, puede investigar el uso de las funciones upper() y lower()
#para transformar la entrada a mayúsculas o minúsculas y evitar así
#posibles errores de validación por este detalle.
#- Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo en
#un rango), es posible que no sea necesario validar el tipo del dato
#ingresado por teclado.
#- Al detectar un dato inválido, el programa debe darle las siguientes
#opciones al usuario:
#** DATO INVÁLIDO **
#1. Reintentar.
#2. Salir.
#- La opción 1. Reintentar le permite al usuario reingresar el dato de manera
#indefinida, siempre mostrando las opciones ante cada intento fallido.
#- La opción 2. Salir finaliza el programa.

import os

centinela = True
dato = 0
while centinela:
    os.system("cls")
    color = input("Ingrese su color favorito:")
    if color.lower() == "rojo":
      print(f"Tu color favorito es {color.upper()}")
    elif color.lower() == "azul":
      print(f"Tu color favorito es {color.upper()}")
    elif color.lower() == "verde":
      print(f"Tu color favorito es {color.upper()}")
    else:  
      print("****DATO INVALIDO****")
      print("1.Reintentar.\n2.Salir.")
    dato = int(input())
    if dato == 2:
        centinela = False


#6. Al implementar programas interactivos, es normal que la pantalla se llene de
#texto, en detrimento de la experiencia de usuario. Para solucionar este
#inconveniente, Python nos provee una función para limpiar la pantalla (notar
#que esto no tendrá ningún efecto sobre la lógica del programa, simplemente
#dejará la terminal de comandos en blanco). El uso de esta función depende del
#sistema operativo que esté utilizando, pero para empezar deberá importar el
#módulo os, escribiendo la siguiente línea al comienzo de su script:

#import os
#Una vez importado el módulo os, ya podrá utilizar la función para limpiar la
#pantalla en cualquier punto de su programa.
#● En Windows:
#os.system('cls')
#● En Linux:
#os.system('clear')
#Modifique todos los ejercicios de este TP para que cada vez que se reintente
#una entrada o se muestre un menú de opciones, la pantalla esté limpia.


celsius()
tu_edad()
menu()
grados()