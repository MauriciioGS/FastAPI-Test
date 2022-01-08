from os import link, name

from sqlalchemy.sql.schema import ForeignKey
from database import Base
from sqlalchemy import Text,Integer,Column

# Tabla Herramientas ----------------------------------------------------------------------------------------------------------

class Tool(Base):
  __tablename__='tools'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  image = Column(Text, nullable=False)
  link = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Tool title={self.title} description={self.description} image={self.image} link={self.link}>"

# Tabla Cursos----------------------------------------------------------------------------------------------------------

class Course(Base):
  __tablename__='courses'
  id = Column(Integer, primary_key=True)
  name = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Text, nullable=False)
  url_course = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Course name={self.name} description={self.description} date={self.date} url_course={self.url_course}>"

# Tabla Talleres ----------------------------------------------------------------------------------------------------------

class Workshop(Base):
  __tablename__='taller'
  id = Column(Integer, primary_key=True)
  name = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Text, nullable=False)
  url_workshop = Column(Text, nullable=False)
  
  def __repr__(self):
    return f"<Workshop name={self.name} description={self.description} date={self.date} url_workshop={self.url_workshop}>"

# Tabla Materiales ----------------------------------------------------------------------------------------------------------

class Material(Base):
  __tablename__='materials'
  id = Column(Integer, primary_key=True)
  name = Column(Text, nullable=False)
  url_image = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Material name={self.name} url_image={self.url_image}>"

# Tabla Temas ----------------------------------------------------------------------------------------------------------

class Topic(Base):
  __tablename__='topics'
  id = Column(Integer, primary_key=True)
  id_material = Column(Integer, nullable=False)
  title = Column(Text, nullable=False)
  url_notes = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Topic id_material={self.id_material} title={self.title} url_notes={self.url_notes}>"
