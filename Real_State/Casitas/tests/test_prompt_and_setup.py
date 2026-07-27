"""Prompt composition and setup helpers — no Ollama, no data required."""

import pytest

from scoring import REQUIRED_COLUMNS, build_prompt, load_buy_box, load_latest_dataset


PROP = {
    "titulo": "Piso en venta en La Luz de 3 habitaciones",
    "precio": 199000,
    "m2": 90,
    "habitaciones": 3,
    "baños": 2,
    "ubicacion": "La Luz, Málaga",
    "estado": "buen estado",
    "año": 1985,
    "ascensor": "sí",
}


class TestBuildPrompt:
    def test_includes_the_property_data(self):
        prompt = build_prompt(PROP)
        assert "199000" in prompt
        assert "90m²" in prompt
        assert "La Luz" in prompt

    def test_without_buy_box_only_generic_tiers(self):
        prompt = build_prompt(PROP)
        assert "INVESTMENT CRITERIA" not in prompt
        assert "85-100" in prompt  # generic tier scale still present

    def test_with_buy_box_injects_the_criteria(self):
        buy_box = "PREMIUM ZONES (location_score 85-100): La Luz, Olletas"
        prompt = build_prompt(PROP, buy_box=buy_box)
        assert "INVESTMENT CRITERIA" in prompt
        assert buy_box in prompt

    def test_asks_for_json_only(self):
        assert "ONLY valid JSON" in build_prompt(PROP)

    def test_truncates_very_long_titles(self):
        prompt = build_prompt({**PROP, "titulo": "x" * 200})
        assert "x" * 61 not in prompt  # capped at 60 chars


class TestSetupHelpers:
    def test_load_buy_box_reads_the_document(self, tmp_path):
        f = tmp_path / "buy_box.md"
        f.write_text("# Buy Box\nPREMIUM ZONES: La Luz", encoding="utf-8")
        assert "PREMIUM ZONES" in load_buy_box(f)

    def test_load_buy_box_fails_clearly_when_missing(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="Buy Box not found"):
            load_buy_box(tmp_path / "nope.md")

    def test_load_latest_dataset_fails_clearly_when_no_files(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="No files matching"):
            load_latest_dataset(str(tmp_path / "activos_*.csv"))

    def test_load_latest_dataset_rejects_incomplete_schema(self, tmp_path):
        bad = tmp_path / "activos_20260101_0000.csv"
        bad.write_text("url,precio\nhttps://x.com/1,199000\n", encoding="utf-8")
        with pytest.raises(ValueError, match="Missing columns"):
            load_latest_dataset(str(tmp_path / "activos_*.csv"))

    def test_load_latest_dataset_picks_the_most_recent(self, tmp_path):
        header = ",".join(REQUIRED_COLUMNS)
        row = ",".join(["x"] * len(REQUIRED_COLUMNS))
        for stamp in ("20260101_0000", "20260524_1341"):
            (tmp_path / f"activos_{stamp}.csv").write_text(
                f"{header}\n{row}\n", encoding="utf-8"
            )
        df = load_latest_dataset(str(tmp_path / "activos_*.csv"))
        assert len(df) == 1
        assert list(df.columns) == REQUIRED_COLUMNS
