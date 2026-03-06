import string

ALFABETO = string.ascii_uppercase
MOD = 26

# ------------------ MATRIZ CLAVE ------------------
K = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

# ------------------ FUNCIONES ------------------

def limpiar(txt):
    txt = txt.upper()
    return "".join(c for c in txt if c in ALFABETO)

def texto_a_nums(txt):
    return [ALFABETO.index(c) for c in txt]

def nums_a_texto(nums):
    return "".join(ALFABETO[n % MOD] for n in nums)

def bloques(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i+n]

def mult_matriz_vector(M, v):
    res = []
    for fila in M:
        suma = 0
        for i in range(len(v)):
            suma += fila[i] * v[i]
        res.append(suma % MOD)
    return res

# -------- inversa modular (necesaria para poder descifrar) --------

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def inverso_mod(a):
    g, x, _ = egcd(a, MOD)
    if g != 1:
        return None
    return x % MOD

def determinante(M):
    return (
        M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
    )

def matriz_inversa(M):
    det = determinante(M)
    inv_det = inverso_mod(det)
    if inv_det is None:
        return None

    # matriz de cofactores transpuesta (adjunta)
    adj = [
        [
            (M[1][1]*M[2][2] - M[1][2]*M[2][1]),
            -(M[0][1]*M[2][2] - M[0][2]*M[2][1]),
            (M[0][1]*M[1][2] - M[0][2]*M[1][1])
        ],
        [
            -(M[1][0]*M[2][2] - M[1][2]*M[2][0]),
            (M[0][0]*M[2][2] - M[0][2]*M[2][0]),
            -(M[0][0]*M[1][2] - M[0][2]*M[1][0])
        ],
        [
            (M[1][0]*M[2][1] - M[1][1]*M[2][0]),
            -(M[0][0]*M[2][1] - M[0][1]*M[2][0]),
            (M[0][0]*M[1][1] - M[0][1]*M[1][0])
        ]
    ]

    inv = []
    for fila in adj:
        nueva = []
        for val in fila:
            nueva.append((val * inv_det) % MOD)
        inv.append(nueva)

    return inv

# ------------------ CIFRAR ------------------

def cifrar(texto):
    texto = limpiar(texto)
    nums = texto_a_nums(texto)

    # relleno con X
    while len(nums) % 3 != 0:
        nums.append(ALFABETO.index('X'))

    resultado = []
    for b in bloques(nums, 3):
        resultado.extend(mult_matriz_vector(K, b))

    return nums_a_texto(resultado)

# ------------------ DESCIFRAR ------------------

def descifrar(texto):
    invK = matriz_inversa(K)
    if invK is None:
        return "No se puede descifrar (matriz inválida)"

    nums = texto_a_nums(texto)

    resultado = []
    for b in bloques(nums, 3):
        resultado.extend(mult_matriz_vector(invK, b))

    return nums_a_texto(resultado)

# ------------------ MENÚ ------------------

print("1) Cifrar")
print("2) Descifrar")
op = input("Elige opción: ")

if op == "1":
    t = input("Texto: ")
    print("Cifrado:", cifrar(t))

elif op == "2":
    t = input("Texto cifrado: ")
    print("Plano:", descifrar(t))

else:
    print("Opción no válida")