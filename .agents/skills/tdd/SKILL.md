---
name: tdd
description: Desarrollo guiado por tests. Úsala antes de agregar o cambiar comportamiento.
---

# TDD

1. **RED**: escribe un test que llame a la función real (no reimplementes su lógica). Córrelo y confirma que falla por la razón esperada.
2. **GREEN**: escribe el código mínimo para que pase.
3. **REFACTOR**: limpia con los tests en verde.
4. Cierra con la skill `verificar`.

```bash
uv run pytest <modulo> -q
```

Un test que nunca viste fallar no prueba nada.
