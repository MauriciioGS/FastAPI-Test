from database import Base
from sqlalchemy import Text,Integer,Column

class Tool(Base):
    __tablename__='tools'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    image = Column(Text, nullable=False)
    link = Column(Text, nullable=False)

def __repr__(self):
    return f"<Tool title={self.title} description={self.description} image={self.image} link={self.link}>"
