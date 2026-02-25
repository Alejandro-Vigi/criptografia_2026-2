import string

def quitar_reptidos(cadena):
    return "".join(dict.fromkeys(cadena))

def insertar_llave(llave):
    letras = string.ascii_uppercase # Crea un arreglo con todas las letras.
    letras = letras.replace('J', "")
    llave = llave.replace('J','I')
    llave = quitar_reptidos(llave)
    matriz_recorrida = [[0 for col in range(5)] for row in range(5)]
    i = 0
    j = 0
    for letra in llave:
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
    return matriz_recorrida

def prep_mensaje(mensaje_original):
    mensaje_procesado = ""
    aux =""
    mensaje_original = mensaje_original.replace('J','I')
    if(len(mensaje_original)%2 == 1):
        mensaje_original += 'X'
    for i in range(len(mensaje_original)):
        aux += mensaje_original[i]
        if(len(aux) == 2):
            if(aux[0]==aux[1]):
                temp = aux[0]
                aux = temp + 'X'
            mensaje_procesado += aux
            aux=""
    return mensaje_procesado

def cifrar(matriz,mensaje):
    posiciones = {matriz[f][c]: (f, c) for f in range(5) for c in range(5)}
    mensaje_cifrado = ""
    aux = ""
    for i in range(len(mensaje)):
        aux += mensaje[i]
        if(i%2==1):
            l1 = aux[0]
            l2 = aux[1]
            f1, c1 = posiciones[l1]
            f2, c2 = posiciones[l2]
            if(f1==f2):
                c1_new =(c1+1)%5
                c2_new =(c2+1)%5
                l1_new = matriz[f1][c1_new]
                l2_new = matriz[f2][c2_new]
            elif(c1==c2):
                f1_new =(f1+1)%5
                f2_new =(f2+1)%5
                l1_new = matriz[f1_new][c1]
                l2_new = matriz[f2_new][c2]
            else:
                l1_new = matriz[f1][c2]
                l2_new = matriz[f2][c1]
            mensaje_cifrado += l1_new
            mensaje_cifrado += l2_new
            aux=""
    return mensaje_cifrado

def descifrar(matriz,mensaje):
    posiciones = {matriz[f][c]: (f, c) for f in range(5) for c in range(5)}
    mensaje_descifrado = ""
    aux = ""
    for i in range(len(mensaje)):
        aux += mensaje[i]
        if(i%2==1):
            l1 = aux[0]
            l2 = aux[1]
            f1, c1 = posiciones[l1]
            f2, c2 = posiciones[l2]
            if(f1==f2):
                l1_new = matriz[f1][c1-1]
                l2_new = matriz[f2][c2-1]
            elif(c1==c2):
                l1_new = matriz[f1-1][c1]
                l2_new = matriz[f2-1][c2]
            else:
                l1_new = matriz[f1][c2]
                l2_new = matriz[f2][c1]
            mensaje_descifrado += l1_new
            mensaje_descifrado += l2_new
            aux=""
    return mensaje_descifrado

mensaje = input("Introduce la palabra que quieres cifrar (únicamente se aceptan letras: en mayúscula, sin acentos -> A-Z): ")
llave = input("Introduce la llave (únicamente se aceptan letras: en mayúscula, sin acentos -> A-Z): ")

print(f"El mensaje que se desea cifrar es: {mensaje}")
matriz_recorrida = insertar_llave(llave)
# print(matriz_recorrida)

mensaje_adaptado = prep_mensaje(mensaje)
print(f"El mensaje adaptado a las restricciones del cifrado de Playfair es: {mensaje_adaptado}")

mensaje_cifrado = cifrar(matriz_recorrida,mensaje_adaptado)
print(f"El mensaje cifrado que se recibe es: {mensaje_cifrado}")

mensaje_descifrado = descifrar(matriz_recorrida,mensaje_cifrado)
print(f"El mensaje descifrado es: {mensaje_descifrado}")