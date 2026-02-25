import string

def quitar_reptidos(cadena):
    return "".join(dict.fromkeys(cadena))

def insertar_clave(clave):
    letras = string.ascii_uppercase # Crea un arreglo con todas las letras.
    letras = letras.replace('J', "")
    clave = clave.replace('J','I')
    clave = quitar_reptidos(clave)
    matriz_recorrida = [[0 for col in range(5)] for row in range(5)]
    i = 0
    j = 0
    for letra in clave:
        if i == 5:
            i = 0
            j += 1
        matriz_recorrida[j][i] = letra
        letras = letras.replace(letra, "")
        i += 1
    for letra in letras:
        if i == 5:
            i = 0
            j += 1
        matriz_recorrida[j][i] = letra
        letras = letras.replace(letra, "")
        i += 1
    print(letras)
    return matriz_recorrida

def prep_mensaje(mensaje_original):
    mensaje_procesado = ""
    aux =""
    if(len(mensaje_original)%2 == 1):
        mensaje_original += 'X'
    print(mensaje_original)
    for i in range(len(mensaje_original)):
        aux += mensaje_original[i]
        if(len(aux) == 2):
            if(aux[0]==aux[1]):
                temp = aux[0]
                aux = temp + 'X'
            mensaje_procesado += aux
            aux=""
    return mensaje_procesado

mensaje = "HELLOWORLD"
clave = "SILLA"

matriz_recorrida = insertar_clave(clave)
print(matriz_recorrida)
mensaje_adaptado = prep_mensaje(mensaje)
print(mensaje_adaptado)