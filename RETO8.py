#8 CONTANDO PALABRAS
"""""
 Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

contador = 0
def contador_palabras(frase):
    #frase en miniscula
    frase = frase.lower()

    contador = 0
    #separar palabras
    for i in frase:
        if i == " ":
            contador = contador + 0
        else:         
            contador = contador + 1
    
    
    return print(contador)

contador_palabras("hola mundo")