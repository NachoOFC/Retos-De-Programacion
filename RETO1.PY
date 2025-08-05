"""
Programa que muestra por consola los números del 1 al 100,
sustituyendo:
- Múltiplos de 3 por "fizz"
- Múltiplos de 5 por "buzz" 
- Múltiplos de 3 y 5 por "fizzbuzz"
"""

print("Números del 1 al 100: ")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# RETO1.PY
# Fin del reto