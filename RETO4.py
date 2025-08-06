#4¿ES UN NÚMERO PRIMO?
""""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
 """

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


for n in range(1, 101):
    if es_primo(n):
        print(n)
