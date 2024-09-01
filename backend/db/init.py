"""
It helps in initializing the database and creates the session
"""
import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

host_name = os.getenv('host_name')
SQLALCHEMY_DATABASE_URL = f"postgresql://root:example@{host_name}:5432/labs_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)

def table_exists(table_name: str) -> bool:
    """
    CHecks if the table exists the database
    
    Args:
        table_name (str): Name of the table
        
    Returns:
        bool: if the table exists or not
    """
    return inspect(engine).has_table(table_name)
