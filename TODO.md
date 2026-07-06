# Repo maintenance TODO

- [ ] **Limpiar historia de git (git filter-repo):** la historia contiene archivos pesados ya eliminados del working tree — `IT-LLM-Job-Finder-Agent_Luis_Dotto.zip` (12MB), `dataset/jobs.csv` (74MB) y `chroma/chroma.sqlite3`. Reescribe la historia del monorepo entero: hacerlo en un momento tranquilo, con backup, y force-push coordinado. Hasta entonces el repo funciona bien, solo pesa de más al clonar.
- [ ] **IT-LLM-Job-Finder-Agent:** subir `assets/cover.png` (screenshot del Chainlit UI con el Jobs Agent respondiendo) — el README ya lo referencia.
- [ ] **IT-LLM-Job-Finder-Agent:** smoke test end-to-end con API key (`etl.py` + `chainlit run` + conversación real).
