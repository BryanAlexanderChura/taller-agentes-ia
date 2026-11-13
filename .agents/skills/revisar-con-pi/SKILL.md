---
name: revisar-con-pi
description: Pide a pi, con un modelo de otro proveedor, que revise el diff actual. Úsala antes de integrar un cambio grande.
---

# Revisar con pi

Un modelo distinto al autor tiene otros puntos ciegos.

```bash
pi -p --no-session --model <proveedor>/<modelo> "Revisa los cambios de 'git diff HEAD' en este repo. Busca solo defectos demostrables: errores de lógica, casos borde, regresiones y cambios fuera de alcance. No edites archivos. Responde una lista: archivo:línea, defecto, cómo se reproduce. Si no hay defectos, dilo."
```

- Elige un modelo de otro proveedor que el que escribió el código.
- Verifica cada hallazgo antes de corregirlo: el reviewer también se equivoca.
- Corrige, y cierra con la skill `verificar`.
