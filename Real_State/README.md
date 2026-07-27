# 🏢 Real Estate

Property valuation and investment analysis — the sector where domain experience (former real estate agent) meets applied AI.

| Project | What it demonstrates | Stack |
|---|---|---|
| [Casitas](Casitas/) | End-to-end investment screener: multi-platform scraping → local LLM scoring against written criteria → bilingual PDF report | Ollama · Mistral 7B · Selenium · pandas · reportlab · uv |
| [Real-Estate-Price-Predictor](Real-Estate-Price-Predictor/) | Price regression on Buenos Aires listings (Properati) | scikit-learn · pandas |
| [Housing-Price-Prediction-Ames](Housing-Price-Prediction-Ames/) | Advanced regression on the Ames housing dataset *(planned)* | — |

**Reading order as a narrative:** Casitas is the flagship — a real problem (a family losing weeks comparing listings by hand) solved end to end, with a local LLM so private data never leaves the machine. The Properati project covers the classic modeling side: predicting price from property features.
