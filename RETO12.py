#12 ELIMINANDO CARACTERES
""""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 """

def eliminar_caracteres(str1, str2):    
    # Para out1: caracteres que están en str1 pero no en str2
    out1 = []
    for char in str1:
        if char not in str2:
            out1.append(char)
    out1 = ''.join(out1)
    
    # Para out2: caracteres que están en str2 pero no en str1
    out2 = []
    for char in str2:
        if char not in str1:
            out2.append(char)
    out2 = ''.join(out2)
    
    print("out1:", out1)
    print("out2:", out2)

# Ejemplo de uso
eliminar_caracteres("hola mundo", "mundo")