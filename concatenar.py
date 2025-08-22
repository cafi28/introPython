# True

# False

# nombre = "Cafi28"
# saludo = "Bienvenido/a a este curso" 

# unir = nombre + " " + saludo  # Concatenar cadenas de texto
# unir2 = f"Bienvenido/a {nombre} a este curso"  # Usando f-strings para formatear cadenas

# print(unir2)


# edad = 18
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")
    
    
    
# ingresar = input("Quien eres? = ") ## Solicita al usuario que ingrese su nombre

# if ingresar.lower() == "Cafi28":
#     print("Bienvenido/a Cafi28")
# else:
#     print("No te conozco, no eres Cafi28")  
    

#Ejercicio extra = Ingresa 3 notas y obten el promedio. Si es mayor a 40 aprueba y si no reprueba.

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))


promedio = (nota1 + nota2 + nota3) / 3

print(round(promedio))

if promedio >= 40:
    print("Aprobaste el ramo")
else:
    print("Reprobaste el ramo")
    