// Plugin de opencode: bloquea comandos destructivos antes de ejecutarlos.
// Usa la misma lista que el hook de Claude Code y Codex.
import { readFileSync } from "node:fs";

const lista = new URL("../../.agents/hooks/bloqueados.txt", import.meta.url);

const patrones = readFileSync(lista, "utf-8")
  .split(/\r?\n/)
  .filter((p) => p.trim() && !p.startsWith("#"))
  .map((p) => new RegExp(p, "i"));

export const Bloquear = async () => ({
  "tool.execute.before": async (input, output) => {
    const texto = JSON.stringify(output.args ?? {});
    const patron = patrones.find((re) => re.test(texto));
    if (patron) {
      throw new Error(`Bloqueado por el hook de seguridad (patrón: ${patron.source}). Busca otra forma o pide permiso.`);
    }
  },
});
