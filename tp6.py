#####################################################################################################
############################### INTRODUCCION A LA PROGRAMACION ######################################
########################ESTRUCTURA ALTERNATIVA Y OPERADORES LOGICOS##################################
#####################################################################################################
#Repositorio: https://github.com/CarlaGonzalezz/trabajos-practicos-unlu.git
#Apellido y nombre: Gonzalez Carla Micaela
#Legajo: 190256
#####################################################################################################



#1. Cree un script que le solicite al usuario ingresar un número por teclado, y
#luego le informe en pantalla si su número es mayor que 10; antes de finalizar
#e independientemente de lo que haya sucedido antes, el script mostrará un
#mensaje de despedida.


numeroEntero = int(input("Ingrese un numero:"))
if (numeroEntero >10):
     print(f"Tu numero {numeroEntero} es mayor que 10!")  

print("¡Saludos!")


#2. Modifique el script anterior para que mantenga el funcionamiento, pero
#ahora, cuando el número no es mayor que 10, también se muestre un
#mensaje “Tu número (N) es menor o igual que 10!”.


numeroEntero = int(input("Ingrese un numero:"))
if  (numeroEntero >=10):
         print(f"Tu numero {numeroEntero} es mayor que 10!")
else:
     print(f"Tu numero {numeroEntero} es menor o igual que 10!")   

print("¡Saludos!")


#3. Cree un script que le solicite al usuario ingresar dos números por teclado, y
#luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
#de que los números sean iguales, y muestre un mensaje acorde.


numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese otro numero:"))

if (numero1 == numero2):
    print(f"Los numeros {numero1} y {numero2} son iguales!")
else:
    resultado = max (numero1, numero2)
    print(f"El numero mayor de {numero1} y {numero2} es {resultado}!")

print("¡Saludos!")


#4. Cree un script que le solicite al usuario ingresar un número por teclado, y le
#informe con un mensaje si su número es positivo, negativo, o 0.


def numeroNegativo():
    x = int(input("Ingrese un numero:"))
    if ( x < 0):
        print("Negativo")
    elif ( x > 0):        
         print("Positivo")
    else: 
        print("Tu numero es 0")
pass
numeroNegativo()


#5. Cree un script que, dado un número de día de la semana ingresado por
#teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
#números y días de la semana es la siguiente:
#1 = Domingo.
#2 = Lunes.
#3 = Martes.
#4 = Miércoles.
#5 = Jueves.
#6 = Viernes.
#7 = Sábado.


numero = int(input("Ingrese un numero:"))
if (numero == 1):
    print("Domingo!")
elif (numero == 2):
    print("Lunes!")
elif (numero == 3):
    print("Martes!")
elif (numero == 4):
    print("Miercoles!")
elif (numero == 5):
    print("Jueves!")
elif (numero == 6):
    print("Viernes!")
elif (numero == 7):
    print("Sabado!")


#6. Cree un script que le solicite a un alumno de la asignatura Introducción a la
#Programación que ingrese las notas de sus dos parciales. Como resultado, se
#le debe informar al alumno su situación, junto con la nota promedio. Las
#reglas para saber la situación de un alumno son las siguientes:
#● Para estar promovido (es decir, cursada aprobada y no requiere
#rendir final), el alumno debe haber aprobado ambos parciales y
#tener un promedio mayor o igual a 8.
#● Para estar regular (cursada aprobada, pero debe rendir final), el
#alumno debe haber aprobado ambos parciales (nota mayor o igual
#a 4).
#● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
#menor que 4 en alguno de ellos), entonces queda en condición de
#libre (es decir, puede rendir un final extendido o recursar).


nota1 = int(input("Ingrese un numero:"))
nota2 = int(input("Ingrese otro numero:"))
promedio = (nota1 + nota2) / 2
if (promedio >= 8):
    print("Promoviste!")
elif (promedio <=3):
    print("Quedaste libre!")
else: 
    print("Aprobaste!")


#7. Cree un script que determine si un triángulo es isósceles, equilátero, o
#escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
#números, correspondientes a los tres lados del triángulo.
#equilátero = todos los lados iguales
#isósceles = dos lados iguales
#escaleno = todos los lados diferentes


def Triangulo(x, y, z):
        if((x < (y + z)) and (y < (x + z)) and (z < (y + x))):
            if((x == y) and (x == z) and (y == z)):
                print("Equilatero") 
            elif((x == y) or (x == z) or (x == z)):
                 print ("Isosceles")
            else:
                print("Escaleno")
Triangulo(10,5,8)


#8. Las estructuras alternativas pueden utilizarse para validar datos. Por
#ejemplo, si se intenta crear una función que tome dos enteros como
#parámetro y muestre el resultado de su división, puede ocurrir un error si el
#denominador es cero. Utilice la estructura alternativa para validar que el
#denominador no sea cero; en caso de serlo, la función deberá mostrar el
#mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
#resultado.


numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese otro numero:"))
if (numero2 <=0):
    print("No se puede dividir por 0!")
elif (numero2 >0):
    resultado = (numero1 / numero2)
    print(f"El resultado de dividir {numero1} y {numero2} es {resultado}")


#9. Python ofrece algunas funciones built-in para facilitar la implementación de
#validaciones. A continuación se listan algunas de las más comunes:
#valor.isdigit()
#Retorna True si todos los caracteres de valor son numéricos, False en caso
#contrario.
#valor.isalpha()
#Retorna True si todos los caracteres de valor son alfabéticos (no
#numéricos), False en caso contrario.
#valor.isalnum()
#Retorna True si valor es una combinación alfanumérica (caracteres y
#números), False en caso contrario.
#Codifique una función que reciba un parámetro cualquiera proveniente del
#usuario del programa (que puede contener letras, números, o una combinación
#de ambas), e indique si el mismo es un número, una palabra, o un valor
#alfanumérico. Compruebe que su función resuelve el problema enviándole
#valores correspondientes a las tres posibilidades.


valor = input("ingrese un dato:")
if (valor.isdigit()):
    print("El dato es numerico.")
elif (valor.isalpha()):
    print("El dato es alfabetico")
elif (valor.isalnum()):
    print("El dato es alfanumerico.")



