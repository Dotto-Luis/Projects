import re
from bs4 import BeautifulSoup

from scrapers.utils import esperar_carga_pagina, empty_listing

def scrape_tecnocasa(driver, url):
    driver.get(url)
    esperar_carga_pagina()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    texto_completo = driver.execute_script("return document.body.innerText;")

    texto_pagina = soup.get_text().lower()
    if "ya no está publicado" in texto_pagina:
        return empty_listing(url, "tecnocasa", "dado de baja")

    try:
        h1s = driver.execute_script("return Array.from(document.querySelectorAll('h1')).map(h => h.innerText.trim());")
        h1s_validos = [h for h in h1s if "archivo" not in h.lower() and len(h) > 10]
        titulo = h1s_validos[0] if h1s_validos else None
    except:
        titulo = soup.find("h1").text.strip() if soup.find("h1") else None

    try:
        ubicacion = titulo.split(" en ")[-1] if titulo and " en " in titulo else titulo
    except:
        ubicacion = titulo

    try:
        precio_text = driver.execute_script("""
            const all = document.querySelectorAll('*');
            for (let el of all) {
                if (el.children.length === 0 && el.innerText &&
                    el.innerText.includes('€') && el.innerText.length < 20) {
                    return el.innerText.trim();
                }
            }
            return null;
        """)
        precio = int(precio_text.replace(".", "").replace("€", "").strip()) if precio_text else None
    except:
        try:
            precio_text = soup.find("span", class_="current-price").text.strip()
            precio = int(precio_text.replace(".", "").replace("€", "").strip())
        except:
            precio = None

    try:
        m2_match = re.search(r'(\d+)\s*m2\b', texto_completo.lower())
        if not m2_match:
            m2_match = re.search(r'(\d+)\s*m²', driver.title)
        m2 = int(m2_match.group(1)) if m2_match else None
    except:
        m2 = None

    try:
        hab_match = re.search(r'(\d+)\s*dormitor', texto_completo.lower())
        habitaciones = int(hab_match.group(1)) if hab_match else None
    except:
        habitaciones = None

    try:
        ban_match = re.search(r'(\d+)\s*baño', texto_completo.lower())
        baños = int(ban_match.group(1)) if ban_match else None
    except:
        baños = None

    try:
        titulos_f = soup.find_all("div", class_="estate-features-title")
        valores_f = soup.find_all("div", class_="estate-features-value")
        features_dict = {t.text.strip().replace(":", "").lower(): v.text.strip()
                        for t, v in zip(titulos_f, valores_f)}
    except:
        features_dict = {}

    try:
        año_raw = features_dict.get("año de construcción", None)
        if not año_raw:
            año_match = re.search(r'(\d{4})', texto_completo)
            año_raw = año_match.group(1) if año_match and 1900 < int(año_match.group(1)) < 2026 else None
        año = int(año_raw) if año_raw and str(año_raw).isdigit() else None
    except:
        año = None

    try:
        comentario = soup.find("div", class_="estate-description").text.strip()
        comentario = comentario.replace("Descripción del inmueble", "").strip()
        if not comentario:
            idx = texto_completo.find("Descripción")
            comentario = texto_completo[idx:idx+500].strip() if idx > 0 else None
    except:
        comentario = None

    texto_ref = (comentario or "") + texto_completo
    planta_match = re.search(r'(\d+)[ªa]\s*planta', texto_ref.lower())
    planta = f"{planta_match.group(1)}ª planta" if planta_match else None
    ascensor = "Sí" if "ascensor" in texto_ref.lower() else "No"

    estado = None
    if "entrar a vivir" in texto_ref.lower() or "llave en mano" in texto_ref.lower():
        estado = "Para entrar a vivir"
    elif "reformado" in texto_ref.lower():
        estado = "Reformado"
    elif "buen estado" in texto_ref.lower():
        estado = "Buen estado"

    tipo = "Casa" if titulo and any(k in titulo.lower() for k in [
        "casa", "chalet", "villa", "adosada", "mata", "unifamiliar"
    ]) else "Piso"

    return {
        "url": url, "plataforma": "tecnocasa",
        "estado_anuncio": "activo",
        "titulo": titulo, "ubicacion": ubicacion, "precio": precio,
        "m2": m2, "habitaciones": habitaciones, "baños": baños,
        "planta": planta, "ascensor": ascensor, "tipo": tipo,
        "estado": estado, "año": año, "anunciante": "Tecnocasa",
        "comentario": comentario
    }