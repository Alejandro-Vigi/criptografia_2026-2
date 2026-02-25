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

mensaje = "HELLOWORLD"
clave = "SILLA"

matriz_recorrida = insertar_clave(clave)
# print(matriz_recorrida)
mensaje_adaptado = prep_mensaje(mensaje)
print(mensaje_adaptado)
mensaje_cifrado = cifrar(matriz_recorrida,mensaje_adaptado)
print(mensaje_cifrado)