#7 INVIRTIENDO CADENAS
""""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""



def cadena_invertida(cadena):
    #dejare el texto en un array 
    array = []
    frase = ""

    for letra in range (len(cadena) -1, -1 ,-1):
       # TODO array.append(cadena[letra])
        frase = frase + cadena[letra]
    

    retorno = frase

    return print(retorno)

    

cadena_invertida("hola mudo")