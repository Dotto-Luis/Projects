"""Pure helpers of the LLM scoring stage — no Ollama, no network."""

import pytest

from scoring import clamp_score, clean_json, normalize_recommendation


class TestCleanJson:
    def test_extracts_json_from_surrounding_prose(self):
        raw = 'Sure! Here is the result:\n{"score_total": 85}\nHope it helps.'
        assert clean_json(raw) == '{"score_total": 85}'

    def test_converts_python_literals_to_json(self):
        raw = '{"ok": True, "bad": False, "missing": None}'
        assert clean_json(raw) == '{"ok": true, "bad": false, "missing": null}'

    def test_raises_when_no_json_present(self):
        with pytest.raises(ValueError, match="No JSON found"):
            clean_json("the model refused to answer")


class TestNormalizeRecommendation:
    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("discarded", "discard"),
            ("discard", "discard"),
            ("visit", "worth_visit"),
            ("worth_visit", "worth_visit"),
            ("opportunity", "strong_opportunity"),
            ("strong_opportunity", "strong_opportunity"),
            ("price_only", "price_only"),
        ],
    )
    def test_maps_llm_variants_to_canonical_tiers(self, raw, expected):
        assert normalize_recommendation(raw) == expected

    def test_is_case_and_whitespace_insensitive(self):
        assert normalize_recommendation("  OPPORTUNITY  ") == "strong_opportunity"

    def test_missing_value_becomes_error(self):
        assert normalize_recommendation(None) == "error"

    def test_unknown_value_passes_through(self):
        # Deliberate: an unmapped tier stays visible instead of being silently dropped
        assert normalize_recommendation("maybe_later") == "maybe_later"


class TestClampScore:
    @pytest.mark.parametrize(
        "raw, expected",
        [(85, 85.0), ("72.5", 72.5), (150, 100), (-10, 0), (0, 0), (100, 100)],
    )
    def test_bounds_score_to_0_100(self, raw, expected):
        assert clamp_score(raw) == expected

    def test_non_numeric_returns_none(self):
        assert clamp_score("not a score") is None
        assert clamp_score(None) is None
