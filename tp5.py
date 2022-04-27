#####################################################################################################
######################## INTRODUCCION A LA PROGRAMACION #############################################
###########################FUNCIONES PROPIAS#########################################################
#####################################################################################################
#Repositorio: https://github.com/CarlaGonzalezz/trabajos-practicos-unlu.git
#Apellido y nombre: Gonzalez Carla Micaela
#Legajo: 190256
################################################################################################################



#1-. Cree una función que reciba dos números como parámetro, y muestre en
#pantalla la suma aritmética de ambos. Invoque a la función con dos números
#leídos desde teclado.


def sumaAritmetica(a, b):
    suma = a + b
    print(f"suma de {a} + {b} es {suma}")
numero1 = int(input("ingrese un numero:")) 
numero2 = int(input("ingrese un numero:"))
sumaAritmetica(numero1, numero2)


#2-. Modifique el script del ejercicio anterior para que la función retorne el resultado
#en vez de mostrarlo. El programa debe seguir mostrando el resultado en
#pantalla.


def sumaAritmetica(a, b):
    suma = a + b
    return suma
a = 10
b = 20
print(sumaAritmetica(a, b))


#3-. Cree una función que reciba un string como parámetro, y retorne la cantidad de
#letras que posee. Luego, utilice la función para escribir un programa que solicite
#ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
#ese nombre.


def contar_nombre(x):
    nombre = len(x)
    return nombre

nombre1 = input("ingrese un nombre:")
print(f"El nombre {nombre1} tiene {contar_nombre(nombre1)} letras.")


#4-. Cree una función que reciba dos números como parámetro (base y exponente),
#y retorne el resultado de elevar base a la potencia exponente.


def potencia(base, exponente):
    resultado = base ** exponente
    return resultado

base = 20
exponente = 5
print(potencia(base, exponente))


#5-. Cree una función que reciba un string como parámetro, y retorne el mismo
#string, pero con todas las letras convertidas a mayúsculas.


def palabra_mayuscula(nombre):
    resultado = nombre.upper()
    return resultado

minuscula = input("Ingrese un nombre:")
mayuscula = palabra_mayuscula(minuscula)
print(mayuscula)


#6-. Modifique la función del ejercicio anterior para que retorne dos versiones del
#string recibido como parámetro: primero la versión en minúsculas, y luego la
#versión en mayúsculas.


def min_mayus(nombre):
    resultado = f"El nombre {nombre.lower()} en mayuscula es {nombre.upper()} "
    return resultado

resultado = input( "ingrese un nombre:")
resultado1 = min_mayus(resultado)
print(resultado1)


#7-.  Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
#y retorne True si nombre1 tiene más letras que nombre2, o False en caso
#contrario.


def nombres(nombre1, nombre2):
    resultado = (len(nombre1)) > (len(nombre2))
    return resultado

nombre1 = input("Ingrese el primer nombre:")
nombre2 = input("Ingrese un segundo nombre:")
resultado = nombres(nombre1, nombre2)
print(f"El nombre {nombre1} tiene {nombre2} : respuesta: {resultado}")


#8-. Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
#llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
#un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
#programa_principal.py, que ejecute el programa haciendo uso de la función
#creada en el otro archivo.

