from sqlmodel import SQLModel, create_engine
from models import *


sqlite_url = "sqlite:///investment.db"

engine = create_engine(sqlite_url)

# Create database and table
SQLModel.metadata.create_all(engine)