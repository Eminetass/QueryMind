"""Veritabanı URL'leri, API anahtarları ve diğer gizli bilgiler gibi ortam tabanlı yapılandırmaları yönetir."""
from pydantic_settings import BaseSettings  # type: ignore
import os


class Settings(BaseSettings):
    DATABASE_HOST: str = 'localhost'
    DATABASE_URL: str = 'postgresql://localhost:5432/mydatabase'
    DATABASE_PORT: str ='5432'  #PostgreSQL varsayılan portu
    MILVUS_HOST: str = 'localhost'       # Milvus bağlantısı için gerekli
    MILVUS_PORT: str = '19530'           # Milvus bağlantı portu
    LOG_FILE_PATH: str = 'logs/app.log'  # Log dosya yolu


    AZURE_OPENAI_EMBEDDING_MODEL: str = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL")
    AZURE_OPENAI_LLM_MODEL: str = os.getenv("AZURE_OPENAI_LLM_MODEL")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "distilbert-base-uncased")

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()