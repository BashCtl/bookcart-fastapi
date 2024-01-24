from src.core.database import engine
from src.models import Base

Base.metadata.create_all(bind=engine)
