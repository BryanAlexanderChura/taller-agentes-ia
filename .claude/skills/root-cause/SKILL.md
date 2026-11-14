---
name: root-cause
description: Encuentra la causa raíz antes de parchear. Úsala cuando un arreglo falla o vas por el tercer parche al mismo problema.
---

# root-cause

Uso: `/root-cause <síntoma>`

## Protocolo

1. **Para.** No más parches ni `print` al azar.
2. **Sigue el dato** desde el síntoma hasta su origen:
   - dónde se ve el error (archivo, línea, valor incorrecto);
   - de dónde viene ese valor (la función que lo produce, la consulta que lo trae);
   - dónde se corrompe: el punto exacto en que deja de ser correcto.
   Si lo que encuentras contradice tu hipótesis, gana lo que encuentras.
3. **Reprodúcelo con un test** que falle por esa causa (skill `tdd`).
4. **Si el rastro no es obvio**, usa un debugger: punto de parada en la función
   sospechosa e inspección de variables donde el dato se corrompe.
5. **Mide el alcance del arreglo**:
   - toca 1 o 2 archivos: arréglalo;
   - toca 3 o más por la misma regla: propone un refactor antes de arreglar;
   - entre candidatos, prefiere el que borra o simplifica sobre el que agrega una guarda.
6. **Sin visión del flujo completo**, pregunta: "¿qué otros procesos consumen este dato?".
   Preguntar es más barato que parchear mal.
7. Cierra con la skill `verificar`.

## Respuesta

- causa raíz, con archivo y línea;
- el test que la reproduce;
- el arreglo y por qué ese y no otro.

## Antipatrón

Parchear el síntoma tres veces en lugar de investigar la causa una vez.
