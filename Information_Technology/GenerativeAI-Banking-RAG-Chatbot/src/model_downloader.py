from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Embedding model
SentenceTransformer('all-MiniLM-L6-v2')

# Language model (CPU-friendly)
model_id = "google/flan-t5-base"
AutoTokenizer.from_pretrained(model_id)
AutoModelForSeq2SeqLM.from_pretrained(model_id)

print("Models downloaded successfully.")
