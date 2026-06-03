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
    palabras =[]
    contador = 0
    #separar palabras
    while frase:
        palabra = ""
        for letra in frase:
            if letra.isalpha(): # Verificar si el carácter es una letra
                palabra += letra
            else:
                break
        if palabra:
            palabras.append(palabra)
        frase = frase[len(palabra):].lstrip() # Eliminar la palabra y los espacios en blanco al inicio
    #contar palabras
    for palabra in palabras:
        contador += 1
        
    
    return print(contador,palabras)

contador_palabras("hola mundo")