#Ejercicio nº2

# %%
print("Hola")
# %%

#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

# %%
def calcular_maximo(a:int,b:int) ->int:
    if a > b:
        return a
    else:
        return b
    
r_1 = calcular_maximo(1,2)
r_2 = calcular_maximo(50,80)

assert r_1 == 2

print (r_1)

#Ejercicio 2: Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
# %%
def calcular_maximo_de_tres (a:int,b:int,c:int) ->int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    
r_1 = calcular_maximo_de_tres(4,6,8)
print(r_1)
r_2 = calcular_maximo_de_tres(20,68,35)
print(r_2)
r_3 = calcular_maximo_de_tres(35,18,58)
print(r_3)
assert r_1 == 8
assert r_2 == 68
assert r_3 == 58
# %%

# Ejercicio 3: Definir una función que calcule la longitud de una lista o una cadena dada.
def contar_caracteres(string) -> int:
    return len(string)

string = "Me llamo Marina"
assert contar_caracteres(string) == 15
print(contar_caracteres(string))
# %%

#Ejercicio 4: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

def es_vocal(caracter: str) -> bool:
    
    vocales = ('a', 'e', 'i', 'o', 'u',)  
    if caracter in vocales:
        return True
    else:
        return False

# Ejemplos de uso
print(es_vocal('a'))  
print(es_vocal('b')) 

# %%

#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 

def sumar_lista (numeros:list) -> int:
    return sum (numeros)
lista = [1,2,3,4]
print(sumar_lista(lista))
# %%
def multiplicar_lista(numeros) -> int:
    resultado = 1
    for numero in numeros:  # Iteramos sobre cada número en la lista 'numeros'
        resultado *= numero  # Multiplicamos 'resultado' por el 'numero' actual
    return resultado

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4]
print(multiplicar_lista(lista_numeros)) 

# %%
