#5 ÁREA DE UN POLÍGONO
"""""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectangulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
   """



def area_poligono(poligono):
    
    
    if poligono == "Triangulo":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
       
    elif poligono == "Cuadrado":
        lado = float(input("Ingrese lado: "))
        area = (lado * lado)
    elif poligono == "Rectangulo":
        lado1 = float(input("Ingrese lado 1: "))
        lado2 = float(input("Ingrese lado 2: "))
        area = (lado1 * lado2)

    return print("el area es : " , area , "\n")




opcion = 0
while opcion != 4:
    if opcion == 1 :
     area_poligono("Triangulo")
    elif opcion == 2:
        area_poligono("Cuadrado")
    elif opcion == 3:
        area_poligono("Rectangulo")

    opcion = int(input("escoja una opcion: \n  1-Triangulo\n  2-Cuadrado\n  3-Rectangulo\n  4-SALIR \n"))

    


