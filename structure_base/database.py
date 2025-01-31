# db_connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

class DatabaseConnection:
    def __init__(self, db_url: str = "sqlite:///./test.db"):
        # URL de la base de datos
        self.db_url = db_url
        self.engine = create_engine(self.db_url, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db_session = None

    def open_connection(self) -> Session:
        """
        Abre una nueva sesión de base de datos
        """
        self.db_session = self.SessionLocal()
        return self.db_session

    def close_connection(self):
        """
        Cierra la sesión de la base de datos
        """
        if self.db_session:
            self.db_session.close()
