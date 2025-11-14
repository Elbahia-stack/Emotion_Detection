from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables depuis .env
load_dotenv()

# Récupérer l'URL de la DB
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas défini. Vérifie ton .env ou tes secrets GitHub.")

# Créer l'engine PostgreSQL
engine = create_engine(DATABASE_URL)

# Créer la session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base pour les modèles
Base = declarative_base()

# Créer les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Dépendance FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
