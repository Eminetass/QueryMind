"""Bu dosya Milvus vektör veritabanı ve LLM ile etkileşim için rota tanımlarını işler."""
from fastapi import APIRouter, Depends, HTTPException, Form
from pymilvus import Status
from configs.settings import settings
from sqlalchemy.orm import Session
from api.auth import create_access_token, verify_password, verify_token
from api.services.milvus_service import create_embedding, search_in_milvus,insert_embeddings,initialize_milvus
from api.services.llm_service import generate_response_with_llm
from models.models import get_db,User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=Status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    return {"username": username}


