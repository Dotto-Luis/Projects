from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# Embedding models
SentenceTransformer('all-MiniLM-L6-v2')

# Language models
model_id = "stabilityai/stablelm-tuned-alpha-3b"
AutoTokenizer.from_pretrained(model_id)
AutoModelForCausalLM.from_pretrained(model_id)
