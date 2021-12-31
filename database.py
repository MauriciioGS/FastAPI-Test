import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine("postgresql://postgres:mauricio@localhost/tool",
#        echo=True
#)

engine = create_engine("postgresql://owncyrupydzcje:f2c62c2a1a93bb1d10eba1730ef05439cb171043838bcfefcec487a7fdc1008e@ec2-34-236-87-247.compute-1.amazonaws.com:5432/dbjigarbn8mqup",
        echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
