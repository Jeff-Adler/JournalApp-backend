from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to SQLite db
SQLALCHEMY_DATABASE_URL = "sqlite:///./JournalApp-backend.db"
# Connect to PostgreSQL db (INSERT POSTGRES DB URL)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create SQLAlchemy engine (connect args argument is SQLite specific)
engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()