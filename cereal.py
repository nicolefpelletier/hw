#This code creates the tables for #3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey
from sqlalchemy import exists
from sqlalchemy import inspect
from sqlalchemy import sql, select, join, desc

engine = create_engine('sqlite:///cereal.sqlit')

metadata = MetaData()


#Try to load in the data, and if it isn't there then create it
try:
  BasicInformation = Table('BasicInformation', metadata, autoload=True)
  
except:
  BasicInformation = Table('BasicInformation', metadata,
    Column('name', String, primary_key=True),
    Column('mfg', String),
    Column('address', String),
    )
  
try:
  NutritionalInformation = Table('NutritionalInformation', metadata, autoload=True)
 
except:
  NutritionalInformation = Table('NutritionalInformation', metadata,
  Column('name', String, ForeignKey('BasicInformation.name')),
  Column('calories', Integer),
  Column('protein', Integer),
  Column('fat', Intger),
  Column('sodium', Integer),
  Column('fiber', Float),
  Column('carbo', Float),
  Column('sugars', Integer),
  Column('potass', Integer),
  Column('vitamins', Integer),
  Column('cups', Float),
  Column('rating', Float),
  Column('address', String)),
  )
  
metadata.create_all(engine)
inspector = inspect(engine)
print(inspector.get_table_names())
