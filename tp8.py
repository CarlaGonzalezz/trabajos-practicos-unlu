#####################################################################################################
######################## INTRODUCCION A LA PROGRAMACION #############################################
########################ESTRUCTURAS REPETITIVAS CONDICIONALES########################################
#####################################################################################################
#Repositorio: https://github.com/CarlaGonzalezz/trabajos-practicos-unlu.git
#Apellido y nombre: Gonzalez Carla Micaela
#Legajo: 190256
#####################################################################################################

#Existen situaciones en las que no está claro, o no es posible conocer con antelación,
#cuántas veces vamos a repetir un bloque de código. En estos casos debemos utilizar
#una estructura que nos permita repetir código “hasta que se cumpla determinada
#condición”. En Python, esa estructura es el while, que tiene la siguiente forma:
#while [condición]:
#código a repetir]

#En donde:
#● while es una palabra reservada que utilizamos para indicar que vamos a repetir
#un bloque de código de manera condicional.
#de cada iteración, de manera que si es verdadero, el bloque se ejecutará una vez
#más, y si es falsa, el bucle finaliza, y el programa continúa su ejecución.
#● El código a repetir es el bloque de instrucciones que se ejecutará en cada
#iteración del bucle (siempre que la condición sea verdadera).
#A las expresiones o variables booleanas que se utilizan como condición de un while se
#las suele llamar bandera, flag, o guarda, entre otros sinónimos.
#Las iteraciones condicionales se pueden utilizar para mejorar la forma en que
#validamos la entrada del usuario, ya que podemos, por ejemplo, repetir el código para
#leer y validar el dato a leer, hasta que el mismo sea válido.

#1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
#usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
#el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
#para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.

def palabras():
    letra = ""
    while(letra != "Parar"):
        letra = input("Ingrese una palabra:")
        print(f"La palabra ingresada es {letra} :")
    print("TERMINADO!")


#2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
#hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
#cargar. Una vez ingresadas las notas, el programa debe informar la nota
#promedio (tenga cuidado de no incluir al -1 dentro del promedio).

def parciales():
    nota1 = 0
    contar = 0
    promedio = 0
    total = 0
    print("Ingrese sus notas, para terminar ingrese -1")
    while(nota1 != -1):
        nota1 = int(input("Ingrese la nota:"))
        if(nota1 != -1):
            total += nota1
            contar += 1
    if(0 >= total):
            print("No ingreso ninguna nota.")
    else:
            promedio = total / contar
            print(f"Su promedio es {promedio}:")


#3. Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
#programa debe ser capaz de solicitarle al usuario que reingrese el número
#cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
#vez que detecte un error de validación, informele al usuario cuál fue el error, con
#los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
#fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
#válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

def valido():
    centinela = True
    while centinela:
        numero = input("Ingrese un numero entre el 1 y el 100:")
        if numero.isdigit():
            if 0 < int(numero) and int(numero) <= 100:
             print(f"{numero} es valido. Gracias!")
             centinela = False
            else:
             print("El numero ingresado esta fuera del rango permitido.")
        else:
            print("El dato ingresado no es numerico.")


#4. Construya un menú que le muestre al usuario lo siguiente:
#********* MI PROGRAMA *********
#1. Saludar.
#2. Informar temperatura.
#3. Mostrar nombre de materia.
#4. Salir.
#Seleccione una opción [1-4]:
#● - Cuando el usuario ingrese la opción 1, se mostrará el mensaje:
#“Hola, bienvenido a mi programa interactivo!”.
#● - Cuando el usuario ingrese la opción 2, se mostrará el mensaje
#“Hay una sensación térmica de 20 grados Celsius.”.
#● - Cuando el usuario ingrese la opción 3, se mostrará el mensaje
#“Estás en la materia Introducción a la Programación!”.
#● - Cuando el usuario ingrese la opción 4, el programa debe terminar,
#mostrando el mensaje “Hasta la próxima!”.
#● - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
#inválida.”.
#Tip 1: crear al menos una función propia, que se encargue exclusivamente
#de mostrar el menú de opciones en pantalla.
#Tip 2: puede utilizar la instrucción os.system('cls') para limpiar la
#pantalla antes de volver a mostrar el menú. De esta manera su programa
#será más legible en la terminal. Para poder utilizar dicha instrucción
#deberá importar, al principio del script, la librería os de la siguiente
#manera:

#import os
# su código

#Tip 3: antes de limpiar la pantalla y volver a mostrar el menú, puede
#esperar a que el usuario confirme que ha terminado de leer la información
#presentada, simplemente utilizando la función

#input(‘PRESIONE ENTER PARA CONTINUAR’).

import os

def programa():
    print("*****MI PROGRAMA***** \n 1. Saludar. \n 2. Informar temperatura. \n 3. Mostrar nombre de materia. \n 4. Salir.")
dato = 0
while dato != 4:
      os.system("cls")
      programa()
      dato = int(input("Seleccione una opcion:"))
      if(dato == 1):
        print("Hola, bienvenido a mi programa interactivo!")
      elif(dato == 2):
        print("Hay una sensacion termica de 20 grados celsius.")
      elif(dato == 3):  
        print("Estas en la materia de Introduccion a la Programacion!")
      elif(dato == 4):
        print("Hasta la proxima!")
      else:
        print("Opcion invalida.")

      input("PRESIONE ENTER PARA CONTINUAR.")


#5. Si bien el while es útil cuando desconocemos la cantidad de veces que
#repetiremos un bloque de instrucciones, también puede ser utilizado en los
#mismos casos que es utilizado el for (aunque la inversa no es verdadera).
#Rehaga todos los ejercicios del Trabajo Práctico VII utilizando un while en
#lugar de un for.

#1. Cree un script para mostrar los primeros 100 números enteros positivos,
#comenzando desde el 1.

#def numeroPositivo():
#    for x in range(1, 101): 
#        print(x)

def numeroPositivo():
    numero = 0 
    while numero <100:
        print(numero)
        numero += 1

#2. Modifique el script del ejercicio anterior para que se muestren sólo los números
#pares. Para saber si un número es par, utilice el operador de módulo (%).

#def numeroPositivo():
#    for x in range(1, 101):
#        if(x % 2 == 0):
#          print(x)

def numerosPositivo():
    numero = 0
    while numero < 100:
        print(numero)
        numero += 2

#3. Cree un script para calcular el resultado de sumar los números desde el 75 al
#150.

#def sumarNumero():
#    numero = 0
#    for x in range(75, 151):
#        numero += x
#    print (numero)

def sumarNumeros():
    numero = 75
    suma = 0
    while numero <= 150:
        suma += numero
        numero += 1 
        
    print(f"La suma total de 75 a 150 es: {suma}")

#4. Cree un script que le solicite al usuario ingresar un número entero, y muestre
#en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
#este ejercicio, pero recuerde que la función range no incluye al valor máximo
#enviado como parámetro.
#factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n

#def numeroEntero():
#    num = int(input("Ingrese un numero:"))
#    num1 = 1
#    x = 0
#    for x in range(1, num+1):
#        num1 *= x
#    print(num1)

def numeroEntero():
  num = int(input("Ingrese un numero:"))
  num1 = 1
  fac = 1
  centinela = True
  while centinela:
    num1 *= fac
    fac += 1
    if (num+1 == fac):
      centinela = False

  print(f"El factorial del numero ingresado es: {num1}")

#5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
#uno, informarle si el mismo es positivo, negativo, o cero.

#def positivo_negativo():
#    numero = 0
#    x = 0
#    for x in range(1, 11):
#        numero = int(input("Ingrese un numero:"))
#        if (numero > 0):
#         print("Positivo")
#        elif (numero < 0):
#            print("Negativo")
#        else:
#            print("Es cero")

def positivo_negativo():
    numero = 0
    x = 0
    centinela = True
    while centinela:
      numero = int(input("Ingrese un numero:"))
      if (numero > 0):
         print("Positivo")
      elif (numero < 0):
            print("Negativo")
      else:
            print("Es cero")
      x += 1
      if x == 10:
          centinela = False




#palabras()
#parciales()
#valido()
#programa()
#numeroPositivo()
#numerosPositivo()
#sumarNumeros()
#numeroEntero()
#positivo_negativo()