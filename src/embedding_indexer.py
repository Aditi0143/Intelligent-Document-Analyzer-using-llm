import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

class EmbeddingIndexer:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.index = None
        self.text_chunks = []

    def embed(self, texts):
        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.numpy()

    def build_index(self, chunks):
        self.text_chunks = chunks
        vectors = self.embed(chunks)
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)

    def query(self, question, top_k=3):
        q_vec = self.embed([question])
        D, I = self.index.search(q_vec, top_k)
        return [self.text_chunks[i] for i in I[0]]