import string
import numpy as np

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

def generar_matriz ():
    m_size = len(lista_letras)
    matriz = np.full((m_size, m_size), "", dtype='U1')
    for i in range(m_size):
        for k in range(m_size):
            if((k+i)<m_size):
                matriz[i][k] = lista_letras[k+i]
            else:
                matriz[i][k] = lista_letras[(k+i)-m_size]
    return matriz

def generar_llave(mensaje,llave_inicial):
    mensaje_tamano = len(mensaje)
    llave_tamano = len(llave_inicial)
    llave=""
    for i in range(mensaje_tamano):
        llave = llave + llave_inicial[i%llave_tamano]
    return llave

def cifrar(mensaje,llave_def,matriz):
    mensaje_cifrado=""
    for i in range(len(mensaje)):
        col=letras_codificado[mensaje[i]]
        ren=letras_codificado[llave_def[i]]
        mensaje_cifrado = mensaje_cifrado + matriz[col][ren]
    return mensaje_cifrado

def descifrar(mensaje_cifrado,llave,matriz):
    mensaje_descifrado=""
    for i in range(len(llave)):
        col = letras_codificado[llave[i]]
        col_llave = matriz[:,col]
        fila_mensaje = np.where(col_llave == mensaje_cifrado[i])[0][0]
        mensaje_descifrado=mensaje_descifrado + lista_letras[fila_mensaje]
    return mensaje_descifrado

lista_letras = list(letras_codificado.keys()) # Crea una lista con las letras del diccionario
matriz_vigenere = generar_matriz() # Crea la matriz que se utiliza para codificar

# Se solicita el mensaje y la llave
mensaje_original = input("Introduce la palabra que quieres cifrar (únicamente se aceptan letras: en mayúscula, sin acentos -> A-Z): ")
llave = input("Introduce la llave (únicamente se aceptan letras: en mayúscula, sin acentos -> A-Z): ")

# Se genera la llave definitiva
llave_def=generar_llave(mensaje_original,llave)
print(f"La llave generada es: {llave_def}")

# Se cifra el mensaje
mensaje_cod = cifrar(mensaje_original,llave_def,matriz_vigenere)
print(f"El mensaje cifrado es: {mensaje_cod}")

# Se descifra el mensaje
mensaje_des = descifrar(mensaje_cod,llave_def,matriz_vigenere)
print(f"El mensaje descifrado es: {mensaje_des}")