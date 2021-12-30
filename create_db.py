from database import Base,engine
from models import Tool

print("Creating database ....")

Base.metadata.create_all(engine)
