from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg:///lab_storage"

engine = create_engine(DATABASE_URL, echo=True)
