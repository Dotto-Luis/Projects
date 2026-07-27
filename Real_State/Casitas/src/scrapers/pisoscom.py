import re
from bs4 import BeautifulSoup

from scrapers.utils import esperar_carga_pagina, empty_listing

def scrape_pisos(driver, url):
    if "alquilar" in url.lower():
        return {
            "url": url, "plataforma": "pisos",
            "estado_anuncio": "alquiler — descartado",
            "titulo": None, "ubicacion": None, "precio": None,
            "m2": None, "habitaciones": None, "baños": None,
            "planta": None, "ascensor": None, "tipo": None,
            "estado": None, "año": None, "anunciante": None,
            "comentario": None
        }

    driver.get(url)
    esperar_carga_pagina()
    soup = BeautifulSoup(driver.page_source, "html.parser")

    texto_pagina = soup.get_text().lower()
    if "ya no está publicado" in texto_pagina:
        return empty_listing(url, "pisos.com", "dado de baja")

    try:
        precio_text = soup.find("div", class_="price__value").text.strip()
        precio = int(re.search(r'[\d\.]+', precio_text).group().replace(".", ""))
    except:
        precio = None

    try:
        titulo = soup.find("h1").text.strip()
    except:
        titulo = None

    try:
        items = soup.find("ul", class_="features-summary").find_all("li", class_="features-summary__item")
        features_texts = [item.text.strip() for item in items]
    except:
        features_texts = []

    m2, habitaciones, baños, planta, ascensor = None, None, None, None, None
    for feat in features_texts:
        feat_lower = feat.lower()
        if "m²" in feat:
            m2_match = re.search(r'(\d+)\s*m²', feat)
            if m2_match: m2 = int(m2_match.group(1))
        elif "habitaci" in feat_lower or "dormitor" in feat_lower:
            hab_match = re.search(r'(\d+)', feat)
            if hab_match: habitaciones = int(hab_match.group(1))
        elif "baño" in feat_lower:
            ban_match = re.search(r'(\d+)', feat)
            if ban_match: baños = int(ban_match.group(1))
        elif "planta" in feat_lower:
            planta = feat
        elif "ascensor" in feat_lower:
            ascensor = "No" if "sin ascensor" in feat_lower else "Sí"

    tipo = "Casa" if titulo and any(k in titulo.lower() for k in ["casa", "chalet", "villa"]) else "Piso"

    try:
        ubicacion = soup.find("span", class_="show-map__address").text.strip()
    except:
        ubicacion = titulo.split(" en ")[-1] if titulo and " en " in titulo else titulo

    try:
        anunciante = soup.find("div", class_="advertiser__name").text.strip()
    except:
        anunciante = None

    try:
        comentario_raw = soup.find("div", class_="description-modal__text") or soup.find("div", class_="js-description")
        comentario = comentario_raw.text.strip()
        if "Traducciones disponibles" in comentario:
            comentario = re.sub(r'Traducciones disponibles.*?Français', '', comentario, flags=re.DOTALL).strip()
            comentario = comentario.split("Mostrar más")[0].strip()
    except:
        comentario = None

    estado, año = None, None
    try:
        for item in soup.find_all("span", class_="features__value"):
            texto = item.text.strip().lower()
            if "buen estado" in texto or "reformado" in texto or "nuevo" in texto:
                estado = item.text.strip()
            año_match = re.search(r'\d{4}', texto)
            if año_match and 1900 < int(año_match.group()) < 2026:
                año = int(año_match.group())
    except:
        pass

    return {
        "url": url, "plataforma": "pisos",
        "estado_anuncio": "activo",
        "titulo": titulo, "ubicacion": ubicacion, "precio": precio,
        "m2": m2, "habitaciones": habitaciones, "baños": baños,
        "planta": planta, "ascensor": ascensor, "tipo": tipo,
        "estado": estado, "año": año, "anunciante": anunciante,
        "comentario": comentario
    }