"""Gömülü kayıtların eklenmesi ve benzer kayıtların aranması gibi Milvus işlemlerini yönetir."""
from pymilvus import Collection, connections,FieldSchema,CollectionSchema,DataType,has_collection
from sqlalchemy.orm import Session
from models import models
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
import os
from configs.settings import settings
import openai


connections.connect("default", host=settings.MILVUS_HOST, port=settings.MILVUS_PORT)

connections.connect("default", host="localhost", port="19530")
print("Milvus is connected!")



model_name = settings.MODEL_NAME
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)



# Embedding oluşturma fonksiyonu
def create_embedding(text):
    """
    Generate embedding from text.
    """
    if isinstance(text, str):
        inputs = tokenizer([text], return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        normalized_embedding = embedding / np.linalg.norm(embedding)
        return normalized_embedding
    else:
        raise ValueError("Input text must be of type `str`.")


# Milvus koleksiyonunun şeması ve oluşturulması
def initialize_milvus():
    """
    Milvus koleksiyonunu oluşturur ve koleksiyon şemasını tanımlar.
    """
    collection_name = "blog_embeddings"
    
    if not has_collection(collection_name):
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768)
        ]
        schema = CollectionSchema(fields, description="Blog metin embedding koleksiyonu")
        collection = Collection(name=collection_name, schema=schema)
        print(f"Milvus koleksiyonu oluşturuldu: {collection_name}")
    else:
        collection = Collection(name=collection_name)
        print(f"Milvus koleksiyonu zaten mevcut: {collection_name}")
    collection.load()



def insert_embeddings(text_data):
    collection_name = "blog_embeddings"

    # Koleksiyonun mevcut olup olmadığını kontrol et
    if not has_collection(collection_name):
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768)
        ]
        schema = CollectionSchema(fields, description="Blog metin embedding koleksiyonu")
        collection = Collection(name=collection_name, schema=schema)
    else:
        collection = Collection(name=collection_name)

    # Embeddingleri oluştur
    embeddings = [create_embedding(str(text)) for text in text_data]
    data = [[i for i in range(len(embeddings))], embeddings]
    collection.insert(data)

    # Dizin oluşturma
    index_params = {
        "metric_type": "L2",       # Vektörler arasındaki mesafeyi hesaplamak için L2 metriğini kullanır
        "index_type": "IVF_FLAT",  # Dizin tipi
        "params": {"nlist": 128}   # Dizin parametresi
    }
    collection.create_index("embedding", index_params)
    collection.load()

    """print("Veriler Milvus'a başarıyla eklendi ve koleksiyon yüklendi.")"""




def search_in_milvus(query_embedding, top_k=3):
    """
    Milvus veritabanında bir embedding'e en yakın top_k sonucu arar.
    """
    collection_name = "blog_embeddings"
    collection = Collection(collection_name)
    collection.load()

    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
    }
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["id", "embedding"]
    )

    if not results or len(results[0]) == 0:
        raise ValueError("Milvus'ta sonuç bulunamadı.")

    # Alınan sonuçları işleyerek sadece ID veya gerekli alanları çekiyoruz
    search_results = [{"id": hit.entity.get("id"), "embedding": hit.entity.get("embedding")} 
                      for hit in results[0] if hit.entity]
    return search_results

