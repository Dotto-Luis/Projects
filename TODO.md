# Repo maintenance TODO

- [ ] **Water-Quality-Prediction: venv commiteado.** `aqua3.10/` está trackeado en git con site-packages completos (cientos de archivos de pandas etc.). Primer paso de su circuito: `git rm -r --cached aqua3.10` + gitignore. También suma peso a la historia (ítem filter-repo).

- [ ] **Limpiar historia de git (git filter-repo):** la historia contiene archivos pesados ya eliminados del working tree — `IT-LLM-Job-Finder-Agent_Luis_Dotto.zip` (12MB), `dataset/jobs.csv` (74MB) y `chroma/chroma.sqlite3`. Reescribe la historia del monorepo entero: hacerlo en un momento tranquilo, con backup, y force-push coordinado. Hasta entonces el repo funciona bien, solo pesa de más al clonar.
- [x] **IT-LLM-Job-Finder-Agent:** cover subido a `images/cover.png`. ✔
- [ ] **IT-LLM-Job-Finder-Agent:** smoke test end-to-end con API key (`etl.py` + `chainlit run` + conversación real).
- [ ] **Perfil GitHub:** actualizar métrica de Home-Credit a 0.754 (LightGBM) y evaluar sumar Banking RAG a featured.
- [ ] **Idea "proyecto casitas" (Real Estate):** proyecto de valuación inmobiliaria aprovechando el background de agente inmobiliario — el segundo sector con edge de dominio después de Finance. Base técnica posible: Kaggle House Prices/Ames (https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques); versión con alma: datos del mercado español (idealista/fotocasa) o argentino. Reemplazaría al viejo Housing-Ames (archivado, solo tenía un readme).
- [ ] **Unificar carpetas de imágenes a `images/` (minúscula)** al pulir cada proyecto: hoy conviven `Images/`, `pics/` y `assets/`. Ojo con el casing en GitHub (case-sensitive) al renombrar: usar `git mv` y actualizar los links de los READMEs.
- [ ] **Migrar a uv los proyectos ya terminados** (otro día, no urgente): `pyproject.toml` + `uv.lock` en IT-LLM-Job-Finder-Agent y Ecommerce-Performance-Insights vía `uv add -r requirements.txt`, y actualizar sus workflows de CI a `astral-sh/setup-uv` + `uv sync`. Los proyectos nuevos ya nacen con uv (empezando por Banking RAG Chatbot).
