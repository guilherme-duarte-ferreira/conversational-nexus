import sqlite3
from contextlib import contextmanager
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_PATH = 'backend/database/nosso_projeto.db'

def ensure_data_directory():
    """Garante que o diretório data/ existe"""
    os.makedirs('backend/database', exist_ok=True)

# Configuração SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    """Inicializa o banco de dados e cria as tabelas se não existirem"""
    ensure_data_directory()
    Base.metadata.create_all(bind=engine)
    
    # Também criamos as tabelas via SQL puro como backup
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                meta JSON
            )
        ''')
        
        db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id)
                ON DELETE CASCADE
            )
        ''')
        db.commit()

@contextmanager
def get_db():
    """Context manager para conexão com o banco"""
    ensure_data_directory()
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()