from sqlalchemy import create_engine

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)

# Bağlantıyı test etme
try:
    with engine.connect() as connection:
        print("Bağlantı başarılı!")
except Exception as e:
    print(f"Bağlantı hatası: {e}")
