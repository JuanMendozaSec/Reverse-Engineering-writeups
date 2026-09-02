📝 Writeup 3: Serial Validation con Checksum
🔐 Descripción

En este ejercicio, el programa no almacena el serial correcto directamente.

En su lugar, valida varias condiciones.

🎯 Objetivo

Comprender el algoritmo de validación y construir una entrada válida.


===============================================================


🔍 Código decompilado

En Ghidra encontramos una función parecida a:

int check_serial(char *serial)
{
    int sum = 0;

    if (strlen(serial) != 10) {
        return 0;
    }

    if (serial[0] != 'R' ||
        serial[1] != 'E' ||
        serial[2] != 'V' ||
        serial[3] != '-') {
        return 0;
    }

    for (int i = 4; i < 10; i++) {
        sum += serial[i];
    }

    if (sum != 360) {
        return 0;
    }

    return 1;
}

===============================================================

🧠 Análisis paso a paso

1️⃣ Longitud
strlen(serial) != 10

El serial debe tener:

10 caracteres

2️⃣ Prefijo

El programa exige:

REV-

Por lo tanto, tenemos:

REV-??????

3️⃣ Checksum

El programa suma los valores ASCII de los últimos seis caracteres:

sum += serial[i];

La suma debe ser:

360

🔢 Buscando una combinación válida

Podemos automatizar la búsqueda con Python.

import itertools
import string

target = 360

chars = string.ascii_uppercase + string.digits

for combination in itertools.product(chars, repeat=6):
    candidate = "".join(combination)

    total = sum(ord(c) for c in candidate)

    if total == target:
        print("REV-" + candidate)
        break


===============================================================
        
🚩 Resultado

El script encuentra una combinación que cumple las condiciones.

Por ejemplo:

REV-AAAA0D

Nota: siempre es importante verificar el resultado contra el binario real.


===============================================================

🔍 Flujo de validación
          Serial
            │
            ▼
   ¿Tiene 10 caracteres?
        │         │
       Sí        No
        │         │
        ▼         ▼
 ¿Empieza con REV-?  Denied
        │
        ▼
 Sumar últimos 6 caracteres
        │
        ▼
 ¿Checksum = 360?
        │
    ┌───┴────┐
   Sí        No
    │         │
    ▼         ▼
 Granted   Denied


===============================================================
 
📚 Lecciones aprendidas
Analizar múltiples condiciones.
Identificar prefijos obligatorios.
Comprender checksums simples.
Interpretar valores ASCII.
Automatizar la búsqueda de entradas válidas.
