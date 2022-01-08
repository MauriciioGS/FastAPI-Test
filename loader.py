from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String
from database import engine

metadata = MetaData(engine)

tool_table = Table('tools', metadata, autoload=True)
course_table = Table('courses', metadata, autoload=True)
workshop_table = Table('workshops', metadata, autoload=True)

