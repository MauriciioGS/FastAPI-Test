from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://pfhlikgnjjhcez:2c9f691a9be547f604f3059adf9993299ecd1cb7c81fbfde8451bb648a2e1bf4@ec2-35-168-80-116.compute-1.amazonaws.com:5432/df6ao8iapi959d",
        echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
