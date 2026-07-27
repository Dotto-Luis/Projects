import re
from bs4 import BeautifulSoup

from scrapers.utils import esperar_carga_pagina, empty_listing

def scrape_idealista(driver, url):
    driver.get(url)
    esperar_carga_pagina()

    soup = BeautifulSoup(driver.page_source, "html.parser")

    texto_pagina = soup.get_text().lower()
    if "ya no está publicado" in texto_pagina:
        return empty_listing(url, "idealista", "dado de baja")

    try:
        precio = int(soup.find("span", class_="info-data-price").find("span", class_="txt-bold").text.strip().replace(".", ""))
    except:
        precio = None

    try:
        titulo = soup.find("span", class_="main-info__title-main").text.strip()
    except:
        titulo = None

    try:
        ubicacion = soup.find("span", class_="main-info__title-minor").text.strip()
    except:
        ubicacion = None

    try:
        features = soup.find_all("div", class_="info-features")
        raw = features[0].text.strip() if features else ""
        partes = [p.strip() for p in raw.split("\n") if p.strip()]
    except:
        partes = []

    m2, habitaciones, planta, ascensor = None, None, None, None
    for parte in partes:
        if "m²" in parte:
            m2 = int(re.search(r'\d+', parte).group())
        elif "hab" in parte:
            habitaciones = int(re.search(r'\d+', parte).group())
        elif "lanta" in parte:
            planta = parte
            ascensor = "No" if "sin ascensor" in parte.lower() else "Sí"

    try:
        caract = soup.find("div", class_="details-property-feature-one")
        caract_items = [li.text.strip() for li in caract.find_all("li")]
    except:
        caract_items = []

    año, estado, baños = None, None, None
    for item in caract_items:
        if "construido en" in item.lower():
            año = int(re.search(r'\d{4}', item).group())
        elif "mano" in item.lower() or "estado" in item.lower():
            estado = item
        elif "baño" in item.lower():
            baños = int(re.search(r'\d+', item).group())

    tipo = "Casa" if titulo and any(k in titulo.lower() for k in [
        "casa", "chalet", "villa", "adosada", "mata", "unifamiliar"
    ]) else "Piso"

    try:
        anunciante = soup.find("div", class_="professional-name").text.strip().replace("Profesional", "").strip()
    except:
        anunciante = None

    try:
        comentario = soup.find("div", class_="comment").text.strip()
        comentario = re.sub(r'\s*Leer comentario completo\s*', '', comentario).strip()
    except:
        comentario = None

    return {
        "url": url, "plataforma": "idealista",
        "estado_anuncio": "activo",
        "titulo": titulo, "ubicacion": ubicacion, "precio": precio,
        "m2": m2, "habitaciones": habitaciones, "baños": baños,
        "planta": planta, "ascensor": ascensor, "tipo": tipo,
        "estado": estado, "año": año, "anunciante": anunciante,
        "comentario": comentario
    }