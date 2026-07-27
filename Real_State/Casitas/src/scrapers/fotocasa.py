import re
from bs4 import BeautifulSoup

from scrapers.utils import esperar_carga_pagina, empty_listing

def scrape_fotocasa(driver, url):
    driver.get(url)
    esperar_carga_pagina()

    soup = BeautifulSoup(driver.page_source, "html.parser")

    texto_pagina = soup.get_text().lower()
    if "ya no está publicado" in texto_pagina:
        return empty_listing(url, "fotocasa", "dado de baja")

    try:
        precio_text = soup.find("span", class_="re-DetailHeader-price").text.strip()
        precio = int(precio_text.replace(".", "").replace("€", "").strip())
    except:
        precio = None

    try:
        titulo = soup.find("h1", class_="re-DetailHeader-propertyTitle").text.strip()
    except:
        titulo = None

    try:
        comentario = soup.find("p", class_="re-DetailDescription").text.strip()
    except:
        comentario = None

    try:
        features_text = soup.find("div", class_="re-ContentDetail-featuresListWrapper").text.strip()
    except:
        features_text = ""

    try:
        header_text = soup.find("div", class_="re-ContentDetail-topContainer--main").text.strip()
    except:
        header_text = ""

    m2_match = re.search(r'(\d+)\s*sqm', header_text)
    m2 = int(m2_match.group(1)) if m2_match else None
    if not m2 and comentario:
        m2_fallback = re.search(r'(\d+)\s*m²', comentario)
        if m2_fallback:
            m2 = int(m2_fallback.group(1))

    hab_match = re.search(r'(\d+)\s*bdrm', header_text)
    habitaciones = int(hab_match.group(1)) if hab_match else None
    if not habitaciones and comentario:
        hab_fallback = re.search(r'(\d+)\s*dormitor', comentario.lower()) or re.search(r'(\d+)\s*habitaci', comentario.lower())
        if hab_fallback:
            habitaciones = int(hab_fallback.group(1))

    ban_match = re.search(r'(\d+)\s*bath', header_text)
    baños = int(ban_match.group(1)) if ban_match else None

    planta_match = re.search(r'(\d+(?:st|nd|rd|th)?\s*[Ff]loor)', header_text)
    planta = planta_match.group(1) if planta_match else None

    ascensor = "Sí" if "LiftYes" in features_text else "No" if "LiftNo" in features_text else None

    estado = None
    if "Good" in features_text: estado = "Buen estado"
    elif "New" in features_text: estado = "Nuevo"
    elif "Renovated" in features_text: estado = "Reformado"

    age_match = re.search(r'Age(\d+)\s*to\s*(\d+)\s*years', features_text)
    año = f"{age_match.group(1)}-{age_match.group(2)} años" if age_match else None

    tipo = "Casa" if titulo and any(k in titulo.lower() for k in [
        "house", "chalet", "villa", "adosada", "mata", "unifamiliar", "casa"
    ]) else "Piso"

    try:
        if "in " in titulo: ubicacion = titulo.split("in ")[-1]
        elif " en " in titulo: ubicacion = titulo.split(" en ")[-1]
        else: ubicacion = titulo
    except:
        ubicacion = titulo

    try:
        anunciante = soup.find("p", class_="re-ContactDetail-name").text.strip()
    except:
        anunciante = None

    return {
        "url": url, "plataforma": "fotocasa",
        "estado_anuncio": "activo",
        "titulo": titulo, "ubicacion": ubicacion, "precio": precio,
        "m2": m2, "habitaciones": habitaciones, "baños": baños,
        "planta": planta, "ascensor": ascensor, "tipo": tipo,
        "estado": estado, "año": año, "anunciante": anunciante,
        "comentario": comentario
    }