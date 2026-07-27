import time
import random
import pandas as pd

from scrapers.config import (
    SOURCES,
    WAIT_PAGE_LOAD,
    WAIT_MIN,
    WAIT_MAX,
    WAIT_LONG,
)


def esperar_entre_requests():
    espera = random.uniform(WAIT_MIN, WAIT_MAX)

    if random.random() < 0.1:
        espera += random.uniform(15, 30)

    time.sleep(espera)


def esperar_carga_pagina():
    time.sleep(random.uniform(*WAIT_PAGE_LOAD))


def esperar_pausa_larga():
    time.sleep(random.uniform(*WAIT_LONG))


def detectar_plataforma(url):
    for nombre, dominio in SOURCES.items():
        if dominio in url:
            return nombre
    return "otro"


def cargar_links(path):
    df = pd.read_csv(path, header=0)
    df.columns = ["url", "extra"]
    df = df[["url"]].dropna()
    df["url"] = df["url"].str.strip()
    df["plataforma"] = df["url"].apply(detectar_plataforma)
    df = df.drop_duplicates(subset="url", keep="first")

    listas = {
        nombre: df[df["plataforma"] == nombre]["url"].tolist()
        for nombre in SOURCES
    }

    return df, listas


def empty_listing(url, plataforma, estado_anuncio):
    return {
        "url": url,
        "plataforma": plataforma,
        "estado_anuncio": estado_anuncio,
        "titulo": None,
        "ubicacion": None,
        "precio": None,
        "m2": None,
        "habitaciones": None,
        "baños": None,
        "planta": None,
        "ascensor": None,
        "tipo": None,
        "estado": None,
        "año": None,
        "anunciante": None,
        "comentario": None,
    }