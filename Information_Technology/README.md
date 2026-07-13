# 💻 Information Technology

Applied AI and ML engineering projects — from LLM agents to computer vision, covering the full lifecycle: data, training, evaluation, serving and front-end.

| Project | What it demonstrates | Stack |
|---|---|---|
| [IT-LLM-Job-Finder-Agent](IT-LLM-Job-Finder-Agent/) | LLM agent with tool-calling + RAG over a job database | LangChain · ChromaDB · Chainlit · OpenAI/Gemini |
| [GenerativeAI-Banking-RAG-Chatbot](GenerativeAI-Banking-RAG-Chatbot/) | Fully local RAG (no API keys, private data stays on-machine) | transformers · flan-t5 · ChromaDB · Tesseract OCR |
| [OpenAI-Agent-Toolkit](OpenAI-Agent-Toolkit/) | Context injection + cost telemetry over the OpenAI API | OpenAI API · pandas |
| [Auto-Image-CNN](Auto-Image-CNN/) | Serving vision models as scalable microservices | Flask · Redis · TensorFlow · Docker · Locust |
| [Vehicle-Inventory-Classification](Vehicle-Inventory-Classification/) | CNN training: from-scratch vs transfer learning (25 classes) | TensorFlow · ResNet50 · scikit-learn |
| [NYCTaxiFarePrediction](NYCTaxiFarePrediction/) | Full-stack ML: training → API → web client (team project) | LightGBM · Flask · Next.js · Docker Compose |

All projects include unit tests, CI (GitHub Actions) and reproducible environments (uv).

**Reading order as a narrative:** the three LLM projects show the grounding spectrum (context injection → RAG → agents with tools); the two vision projects split the ML lifecycle (Vehicle-Inventory = training, Auto-Image-CNN = serving); NYC Taxi puts it all together end-to-end with a real UI.
