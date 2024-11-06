"""Bu dosya Milvus vektör veritabanı ve LLM ile etkileşim için rota tanımlarını işler."""
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from api.services.milvus_service import create_embedding, search_in_milvus,insert_embeddings,initialize_milvus
from api.services.llm_service import generate_response_with_llm
from models.models import get_db
import os

router = APIRouter()

@router.post("/query/")
def query_route(query: str):
    try:
        # Kullanıcı sorgusunu embedding hale getir
        query_embedding = create_embedding(query)
        
        # Milvus'tan en alakalı sonuçları getir
        search_results = search_in_milvus(query_embedding)
        
        # LLM kullanarak yanıt oluştur
        if search_results:
            llm_response = generate_response_with_llm(search_results)
            return {"response": llm_response}
        else:
            return {"response": "Arama sonuçları bulunamadı."}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.on_event("startup")
def load_data_on_startup():
    """
    Proje başlatıldığında AL.txt dosyasındaki verileri embedding yaparak Milvus veritabanına kaydeder.
    """
    file_path = os.path.join("data", "AL.txt")
    embeddings = []
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text_data = file.readlines()
            for line in text_data:
                embedding = create_embedding(line.strip())
                embeddings.append(embedding)
                
        insert_embeddings(embeddings)  # Embeddingleri topluca Milvus'a ekler
