
📝 Writeup 1: Password Validation con Transformación
🔐 Descripción

En este desafío, la contraseña no aparece directamente en texto plano. El programa transforma cada carácter de nuestra entrada antes de compararlo con unos valores almacenados.

🎯 Objetivo

Analizar el algoritmo y recuperar la contraseña correcta.

🛠️ Herramientas utilizadas
Ghidra
Python
x64dbg (opcional)



🔍 Análisis inicial

Al ejecutar el programa obtenemos:

================================
       SIMPLE CRACKME
================================

Enter password: test

[-] Access Denied!

Abrimos el ejecutable con Ghidra y analizamos la función principal.



Encontramos una función similar a esta:

int check_password(char *input)
{
    unsigned char expected[] = {
        0x49, 0x66, 0x64, 0x75,
        0x69, 0x48, 0x71, 0x70
    };

    if (strlen(input) != 8) {
        return 0;
    }

    for (int i = 0; i < 8; i++) {
        unsigned char transformed;

        transformed = (input[i] + 3) ^ 0x20;

        if (transformed != expected[i]) {
            return 0;
        }
    }

    return 1;
}


🧠 Comprendiendo la validación

El programa primero verifica la longitud:

if (strlen(input) != 8)

Por lo tanto, sabemos que la contraseña debe tener:

8 caracteres

Después, cada carácter pasa por esta operación:

transformed = (input[i] + 3) ^ 0x20;

Y el resultado se compara con:

49 66 64 75 69 48 71 70

===============================================================


🔄 Invirtiendo el algoritmo

La operación original es:

(input + 3) XOR 0x20 = expected

Para recuperar el carácter original debemos invertir las operaciones.

Sabemos que XOR es reversible:

A XOR B XOR B = A

Por lo tanto:

input + 3 = expected XOR 0x20

Finalmente:

input = (expected XOR 0x20) - 3

===============================================================

🐍 Recuperando la contraseña con Python

Podemos automatizar el proceso:

expected = [
    0x49, 0x66, 0x64, 0x75,
    0x69, 0x48, 0x71, 0x70
]

password = ""

for byte in expected:
    original = (byte ^ 0x20) - 3
    password += chr(original)

print(password)

Ejecutamos:

python solve.py

Resultado:

fCARFeNM


===============================================================

🚩 Verificación

Introducimos la contraseña recuperada:

Enter password: fCARFeNM

[+] Access Granted!

===============================================================
🔍 Método de resolución

El flujo del análisis fue:

Ejecutar el binario
        ↓
Analizarlo con Ghidra
        ↓
Encontrar la función de validación
        ↓
Identificar la longitud requerida
        ↓
Identificar la transformación
        ↓
Invertir las operaciones
        ↓
Crear un script en Python
        ↓
Recuperar la contraseña

===============================================================

📚 Lecciones aprendidas

En este ejercicio aprendí a:

Analizar una función de validación.
Identificar arrays de bytes.
Comprender operaciones XOR.
Invertir operaciones matemáticas.
Automatizar la solución con Python.
No depender únicamente de strings.
