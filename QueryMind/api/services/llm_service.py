"""Alınan Milvus sonuçlarını LLM'ye besleyerek yanıtlar üretir."""
import os
import openai
from dotenv import load_dotenv
from api.services.milvus_service import (
    initialize_milvus,create_embedding,search_in_milvus,insert_embeddings
)
from configs.settings import settings
from sqlalchemy.orm import Session
import numpy as np

load_dotenv()

openai.api_key = settings.AZURE_OPENAI_API_KEY
openai.api_version =settings.AZURE_OPENAI_API_VERSION
openai.api_type=settings.AZURE_OPENAI_ENDPOINT
openai.embeddings = settings.AZURE_OPENAI_EMBEDDING_MODEL
openai.api_type = "azure"


def generate_response_with_llm(search_results):
        # Milvus'tan gelen arama sonuçlarını kullanarak LLM yanıtı üretir.

  
    try:
        prompt_texts = "\n".join([str(result) for result in search_results if result is not None])
        prompt = f"Aşağıdaki bilgilere dayanarak en iyi yanıtı oluştur:\n{prompt_texts}\n\nSoruya yanıt:"
        print(prompt)

        response = openai.ChatCompletion.create(
            engine=settings.AZURE_OPENAI_LLM_MODEL,
              messages=[
                {"role": "user", "content": search_results}
            ],
            prompt=prompt,
            max_tokens=500,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error while generating response: {e}")
        return "Bir hata oluştu, lütfen tekrar deneyin."
