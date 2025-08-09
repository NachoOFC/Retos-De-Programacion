#11 EXPRESIONES EQUILIBRADAS
""""
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 """

def expresiones_equilibradas(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in expresion:
        if char in pares.values():  # Si es un delimitador de apertura
            pila.append(char)
        elif char in pares.keys():  # Si es un delimitador de cierre
            if not pila or pila[-1] != pares[char]:
                return False  # No hay coincidencia o la pila está vacía
            pila.pop()  # Coincidencia encontrada, quitar el último de la pila
    
    return len(pila) == 0  # Si la pila está vacía, está equilibrada

# Ejemplo de uso
print(expresiones_equilibradas("{ [ a * ( c + d ) ] - 5 }"))  # Debería devolver True
print(expresiones_equilibradas("{ a * ( c + d ) ] - 5 }"))  # Debería devolver False