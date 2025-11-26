from sqlmodel import create_engine, SQLModel
import sqlite3


engine = create_engine("sqlite3:///shibolim.db", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)