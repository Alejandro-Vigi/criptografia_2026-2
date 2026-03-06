import string
import random

def string_to_ascii(letra):
    ascii_value = ord(letra)
    return ascii_value

def ascii_to_byte(ascii_value):
    ascii_value_str = str(ascii_value)
    if(len(ascii_value_str)==2):
        bits_1 = f"{int(ascii_value_str[0]):04b}"
        bits_2 = f"{int(ascii_value_str[1]):04b}"
    else:
        ascii_value_1 = str(ascii_value_str[0])
        ascii_value_2 = str(ascii_value_str[1])
        ascii_value_complete = ascii_value_1 + ascii_value_2
        ascii_value_new = int(ascii_value_complete)
        bits_1 = f"{ascii_value_new:04b}"
        bits_2 = f"{int(ascii_value_str[2]):04b}"
    byte = bits_1 + bits_2
    return byte

def bits_to_str(cadena_bytes):
    tam = int(len(cadena_bytes)/8)
    byte_p1 = ""
    byte_p2 = ""
    cadena_string = ""
    j=0
    for i in range(tam):
        ascii_completo=""
        byte_p1=""
        byte_p2=""
        for k in range(8):
            if(k<=3):
                byte_p1 += cadena_bytes[j]
            else:
                byte_p2 += cadena_bytes[j]
            j+=1
        ascii_1 = str(int(byte_p1,2))
        ascii_2 = str(int(byte_p2,2))
        ascii_completo = ascii_1 + ascii_2
        ascii_letra = chr(int(ascii_completo))
        cadena_string += ascii_letra
    return cadena_string
        

def generar_cadena(palabra):
    cadena = ""
    for i in range(len(palabra)):
        letra_ascii = string_to_ascii(palabra[i])
        ascii_bytes = ascii_to_byte(letra_ascii)
        cadena += ascii_bytes
    return cadena
        

def xor_op(mensaje,llave):
    mensaje_resultado=""
    i=0
    for i in range(len(mensaje)):
        xor_resultado = (int(mensaje[i])+int(llave[i]))%2
        mensaje_resultado += str(xor_resultado)
    return mensaje_resultado

def generar_llave(mensaje):
    random_key = ""
    rango_1 = (65,90)
    rango_2 = (97,122)
    for i in range(len(mensaje)):
        rango = random.choice([rango_1,rango_2])
        random_key_char = random.randint(rango[0],rango[1])
        random_key += chr(random_key_char)
    return random_key

def verificar_mensaje(mensaje):
    for i in range(len(mensaje)):
        mensaje_ascii = ord(mensaje[i])
        if (mensaje_ascii >= 65 and mensaje_ascii <= 90):
            flag = 1
        elif(mensaje_ascii >= 97 and mensaje_ascii <= 122):
            flag = 1
        elif(mensaje_ascii == 32):
            flag = 1
        else:
            flag = 0
            break
    return flag

mensaje_ejemplo = "Cifrado de Verman"
mensaje_valido = verificar_mensaje(mensaje_ejemplo)
if (mensaje_valido == 1):
    print(f"El mensaje que se desea cifrar es: {mensaje_ejemplo}")
    llave = generar_llave(mensaje_ejemplo)
    print(f"La llave generada aleatoriamente es: {llave}")
    mensaje_bytes = generar_cadena(mensaje_ejemplo)
    llave_bytes = generar_cadena(llave)
    mensaje_cifrado_bytes = xor_op(mensaje_bytes,llave_bytes)
    mensaje_cifrado = bits_to_str(mensaje_cifrado_bytes)
    print(f"El mensaje cifrado es: {mensaje_cifrado}")
    mensaje_descifrado_bytes = xor_op(mensaje_cifrado_bytes,llave_bytes)
    mensaje_descifrado = bits_to_str(mensaje_descifrado_bytes)
    print(f"El mensaje descifrado es: {mensaje_descifrado}")
else:
    print("Mensaje inválido")