#13 ¿ES UN PALÍNDROMO?
""""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""


def es_palindromo(texto):
    import unicodedata
    # Normalizar el texto para eliminar tildes y convertir a minúsculas
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()
    
    # Eliminar espacios y signos de puntuación
    texto = ''.join(c for c in texto if c.isalnum())
    
    # Verificar si el texto es igual a su reverso
    return texto == texto[::-1] 

# Ejemplo de uso
print(es_palindromo("Ana lleva al oso la avellana."))  # Debería devolver True
print(es_palindromo("Esto no es un palíndromo"))  # Debería devolver False