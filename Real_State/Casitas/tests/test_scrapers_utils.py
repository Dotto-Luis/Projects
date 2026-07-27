"""Platform detection, listing schema and WhatsApp/chat link extraction.

No network, no browser, no real chat export: the extractor is fed a synthetic
conversation built inside the test.
"""

import pytest

from scrapers.utils import detectar_plataforma, empty_listing
from scrapers.whatsapp_extractor import es_valido, extraer_links_chat


class TestDetectarPlataforma:
    @pytest.mark.parametrize(
        "url, expected",
        [
            ("https://www.idealista.com/inmueble/1234/", "idealista"),
            ("https://www.fotocasa.es/es/comprar/vivienda/malaga/1/d", "fotocasa"),
            ("https://www.pisos.com/comprar/piso-malaga/", "pisos"),
            ("https://www.yaencontre.com/venta/piso/inmueble-1", "yaencontre"),
            ("https://www.tecnocasa.es/venta/piso/malaga.html", "tecnocasa"),
            ("https://www.habitaclia.com/comprar-piso-malaga.htm", "habitaclia"),
        ],
    )
    def test_recognizes_every_supported_platform(self, url, expected):
        assert detectar_plataforma(url) == expected

    def test_unknown_domain_falls_back_to_otro(self):
        assert detectar_plataforma("https://example.com/piso") == "otro"


class TestEmptyListing:
    def test_keeps_identity_fields_and_nulls_the_rest(self):
        row = empty_listing("https://x.com/1", "idealista", "inactivo")

        assert row["url"] == "https://x.com/1"
        assert row["plataforma"] == "idealista"
        assert row["estado_anuncio"] == "inactivo"
        # Every scraped attribute must be present as None so the CSV schema
        # stays stable across platforms.
        for field in ("titulo", "ubicacion", "precio", "m2", "habitaciones", "año"):
            assert row[field] is None

    def test_schema_matches_the_pipeline_contract(self):
        expected = {
            "url", "plataforma", "estado_anuncio", "titulo", "ubicacion",
            "precio", "m2", "habitaciones", "baños", "planta", "ascensor",
            "tipo", "estado", "año", "anunciante", "comentario",
        }
        assert expected.issubset(set(empty_listing("u", "p", "e")))


class TestEsValido:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.idealista.com/alquiler-viviendas/malaga/",
            "https://www.fotocasa.es/es/alquilar/vivienda/malaga/1/d",
            "https://www.idealista.com/obra-nueva/malaga/",
            "https://www.idealista.com/venta-terrenos/malaga/",
        ],
    )
    def test_rejects_rentals_new_builds_and_land(self, url):
        assert es_valido(url) is False

    def test_accepts_a_regular_sale_listing(self):
        assert es_valido("https://www.idealista.com/inmueble/108439614/") is True


class TestExtraerLinksChat:
    def test_extracts_only_valid_listing_urls_and_deduplicates(self, tmp_path):
        chat = tmp_path / "fake_chat.txt"
        chat.write_text(
            "[01/01/26, 10:00:00] A: look at this\n"
            "https://www.idealista.com/inmueble/111/\n"
            "[01/01/26, 10:01:00] B: and this one\n"
            "https://www.fotocasa.es/es/comprar/vivienda/malaga/222/d\n"
            "[01/01/26, 10:02:00] A: duplicate\n"
            "https://www.idealista.com/inmueble/111/\n"
            "[01/01/26, 10:03:00] B: a rental, should be skipped\n"
            "https://www.idealista.com/alquiler-viviendas/malaga/\n"
            "[01/01/26, 10:04:00] A: unrelated link\n"
            "https://www.youtube.com/watch?v=abc\n",
            encoding="utf-8",
        )

        links = extraer_links_chat(str(chat))

        assert links == [
            "https://www.idealista.com/inmueble/111/",
            "https://www.fotocasa.es/es/comprar/vivienda/malaga/222/d",
        ]

    def test_returns_empty_list_for_a_chat_without_listings(self, tmp_path):
        chat = tmp_path / "empty_chat.txt"
        chat.write_text("[01/01/26, 10:00:00] A: hello\n", encoding="utf-8")
        assert extraer_links_chat(str(chat)) == []
