#10 CÓDIGO MORSE
""""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 """


def transformacion(frase):
    morse_diccionario = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': "---..",  
        '9': "----."
    }


    morse_inverso = {v: k for k, v in morse_diccionario.items()}
    frase = frase.upper()
    if all(char in morse_diccionario.values() for char in frase.split()):
        #convertir de Morse a texto
        palabras = frase.split('  ')
        resultado = []
        for palabra in palabras:
            letras = palabra.split()
            resultado.append(''.join(morse_inverso[letra] for letra in letras))
        print(' '.join(resultado))
    else:
        #convertir de texto a Morse
        resultado = []
        for char in frase:
            if char in morse_diccionario:
                resultado.append(morse_diccionario[char])
            elif char == ' ':
                resultado.append('  ')  # Dos espacios para separar palabras
        print(' '.join(resultado))
    return

transformacion(".... --- .-.. .-    -- ..- -. -.. ---")  


