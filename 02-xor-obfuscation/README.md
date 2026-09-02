📝 Writeup 2: XOR Obfuscation
🔐 Descripción

En este desafío, la contraseña se encuentra almacenada como bytes ofuscados mediante XOR.

🎯 Objetivo

Identificar la clave XOR y recuperar el texto original.


===============================================================

🔍 Análisis en Ghidra

Encontramos una función similar a:

int check_password(char *input)
{
    unsigned char encrypted[] = {
        0x1B, 0x3A, 0x28, 0x2E,
        0x0D, 0x3B, 0x2B, 0x3B
    };

    unsigned char key = 0x5A;

    if (strlen(input) != 8) {
        return 0;
    }

    for (int i = 0; i < 8; i++) {
        if ((input[i] ^ key) != encrypted[i]) {
            return 0;
        }
    }

    return 1;
}

===============================================================

🧠 Identificando el algoritmo

La comparación importante es:

(input[i] ^ 0x5A) != encrypted[i]

Esto significa:

input XOR key = encrypted

Como XOR es reversible:

encrypted XOR key = input


===============================================================

🐍 Script de resolución
encrypted = [
    0x1B, 0x3A, 0x28, 0x2E,
    0x0D, 0x3B, 0x2B, 0x3B
]

key = 0x5A

password = ""

for byte in encrypted:
    password += chr(byte ^ key)

print(password)

🚩 Resultado
AbctWaqa

===============================================================


📚 Lecciones aprendidas
Reconocer patrones XOR en código decompilado.
Identificar una clave constante.
Invertir una operación XOR.
Crear scripts para automatizar tareas de reversing.
