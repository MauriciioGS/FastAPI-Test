from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String
from database import engine
import pandas as pd

dict_from_csv = pd.read_csv('./CSV_files/Tools.csv').to_dict()
print(dict_from_csv["title"][0])

metadata = MetaData(engine)

tool_table = Table('tools', metadata, autoload=True)
course_table = Table('courses', metadata, autoload=True)
workshop_table = Table('workshops', metadata, autoload=True)

#ins = tool_table.insert()

#ins = ins.values(title='Un curso',description='Una desc',image='Una url imagen',link='Una url de tool')

conn = engine.connect()
conn.execute(tool_table.insert(), dict_from_csv)