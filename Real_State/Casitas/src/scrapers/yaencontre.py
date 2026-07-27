import re
from bs4 import BeautifulSoup

from scrapers.utils import esperar_carga_pagina, empty_listing

def scrape_yaencontre(driver, url):
    driver.get(url)
    esperar_carga_pagina()

    soup = BeautifulSoup(driver.page_source, "html.parser")

    texto_pagina = soup.get_text().lower()
    if "ya no está publicado" in texto_pagina:
        return empty_listing(url, "yaencontre", "dado de baja")

    try:
        stats_js = driver.execute_script("""
            const header = document.querySelector('.details-header-info');
            return header ? header.innerText : null;
        """)
        stats_text = stats_js.replace('\xa0', ' ')
        stats_clean = stats_text.split("Calcula tu hipoteca")[-1].strip()
    except:
        stats_text = ""
        stats_clean = ""

    try:
        precio_match = re.search(r'([\d\.]+)\s*€', stats_text)
        precio = int(precio_match.group(1).replace(".", "")) if precio_match else None
    except:
        precio = None

    try:
        m2_match = re.search(r'(\d+)\s*m²', stats_clean)
        m2 = int(m2_match.group(1)) if m2_match else None
    except:
        m2 = None

    try:
        numeros = re.findall(r'\b(\d+)\b', stats_clean.split('m²')[0])
        numeros_validos = [int(n) for n in numeros if 0 < int(n) < 20]
        habitaciones = numeros_validos[0] if len(numeros_validos) > 0 else None
        baños = numeros_validos[1] if len(numeros_validos) > 1 else None
    except:
        habitaciones, baños = None, None

    try:
        titulo = soup.find("h1").text.strip()
    except:
        titulo = None

    try:
        ubicacion = titulo.split(" en ")[-1].split(" de ")[0] if titulo and " en " in titulo else titulo
    except:
        ubicacion = titulo

    try:
        features = soup.find_all("li", class_="feature")
        features_dict = {}
        for f in features:
            texto = f.text.strip()
            if ":" in texto:
                key, val = texto.split(":", 1)
                features_dict[key.strip().lower()] = val.strip()
            else:
                features_dict[texto.lower()] = True
    except:
        features_dict = {}

    planta = None
    for key in features_dict:
        if key.startswith("planta"):
            planta = key
            break

    try:
        año_raw = features_dict.get("año de construcción", None)
        año = int(año_raw) if año_raw and año_raw.isdigit() else None
    except:
        año = None

    estado = features_dict.get("estado", None)
    ascensor = "Sí" if "ascensor" in features_dict else "No"
    tipo = "Casa" if titulo and any(k in titulo.lower() for k in [
        "casa", "chalet", "villa", "adosada", "mata", "unifamiliar"
    ]) else "Piso"

    try:
        comentario = soup.find("div", class_="readMoreText").text.strip()
    except:
        comentario = None

    try:
        anunciante = soup.find("div", class_="agency-name").text.strip()
    except:
        anunciante = None

    return {
        "url": url, "plataforma": "yaencontre",
        "estado_anuncio": "activo",
        "titulo": titulo, "ubicacion": ubicacion, "precio": precio,
        "m2": m2, "habitaciones": habitaciones, "baños": baños,
        "planta": planta, "ascensor": ascensor, "tipo": tipo,
        "estado": estado, "año": año, "anunciante": anunciante,
        "comentario": comentario
    }