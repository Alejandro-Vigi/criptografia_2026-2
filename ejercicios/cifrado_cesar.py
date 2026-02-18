import string

letras = string.ascii_uppercase # Crea un arreglo con todas las letras.

letras_codificado = { # Crea un diccionario con cada letra y su posición correspondiente.
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "J" : 9,
    "K" : 10,
    "L" : 11,
    "M" : 12,
    "N" : 13,
    "O" : 14,
    "P" : 15,
    "Q" : 16,
    "R" : 17,
    "S" : 18,
    "T" : 19,
    "U" : 20,
    "V" : 21,
    "W" : 22,
    "X" : 23,
    "Y" : 24,
    "Z" : 25
}

def cifrar(mensaje, recorrido): # Recibe un mensaje a cifrar y el numero de letras a recorrer.
    print("Mensaje a cifrar:", mensaje)
    mensaje_cifrado = "" # Inicializa el mensaje cifrado.
    for llave, valor in letras_codificado.items():
        letras_codificado[llave] = (valor + recorrido) % 26
    for letra in mensaje: # Recorre cada letra en el mensaje a cifrar.
        mensaje_cifrado+=letras[letras_codificado[letra]] # Añade la letra correspondiente a la cadena del mensaje cifrado.
    return mensaje_cifrado # Regresa el mensaje cifrado.

def descifrar(mensaje, recorrido):
    print("Mensaje a descifrar:", mensaje)
    mensaje_descifrado = ""
    for llave, valor in letras_codificado.items():
        letras_codificado[llave] = (valor - recorrido * 2 + 26) % 26
    for letra in mensaje:
        mensaje_descifrado+=letras[letras_codificado[letra]]
    return mensaje_descifrado

mensaje_original = input("Introduce la palabra que quieres cifrar (únicamente se aceptan letras: en mayúscula, sin acentos -> A-Z): ")
recorrido = int(input("\nIntroduce la cantidad de posiciones que deseas recorrer: "))
mensaje_cifrado = cifrar(mensaje_original,recorrido)
print("Mensaje Cifrado:", mensaje_cifrado) # Imprime el mensaje cifrado.
mensaje_descifrado = descifrar(mensaje_cifrado, recorrido)
print("Mensaje Descifrado:", mensaje_descifrado)